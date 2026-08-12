from flask import Flask, render_template, request, redirect, jsonify
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from dotenv import load_dotenv
import os
import json
import uuid
import hashlib
import logging
from pathlib import Path

load_dotenv()

app = Flask(__name__)

# --------------------------------------------------
# Logging configuration
# --------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s"
)

logger = logging.getLogger("flask-mongodb-assignment")

# --------------------------------------------------
# MongoDB configuration
# --------------------------------------------------
mongo_uri = os.getenv("MONGO_URI")

if not mongo_uri:
    logger.error("MONGO_URI environment variable is not configured")
    client = None
    database = None
    collection = None
    todo_collection = None
else:
    try:
        client = MongoClient(
            mongo_uri,
            serverSelectionTimeoutMS=5000
        )

        # Verify MongoDB connection
        client.admin.command("ping")

        database = client["studentDB"]
        collection = database["students"]
        todo_collection = database["todoitems"]

        logger.info("MongoDB connection established successfully")

    except PyMongoError as exc:
        logger.exception("MongoDB connection failed: %s", exc)
        client = None
        database = None
        collection = None
        todo_collection = None


# --------------------------------------------------
# Helper functions
# --------------------------------------------------
def validate_text(value, field_name, max_length=200):
    """Validate required text input."""
    if not isinstance(value, str):
        raise ValueError(f"{field_name} must be text")

    value = value.strip()

    if not value:
        raise ValueError(f"{field_name} is required")

    if len(value) > max_length:
        raise ValueError(
            f"{field_name} must not exceed {max_length} characters"
        )

    return value


def mongo_available():
    """Check whether MongoDB is available."""
    if collection is None or todo_collection is None:
        return False

    try:
        client.admin.command("ping")
        return True
    except PyMongoError:
        logger.exception("MongoDB health check failed")
        return False


# --------------------------------------------------
# Routes
# --------------------------------------------------
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/todo")
def todo():
    return render_template("todo.html")


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/health")
def health():
    """Health endpoint for monitoring and load balancers."""
    if mongo_available():
        return jsonify({
            "status": "healthy",
            "mongodb": "connected"
        }), 200

    return jsonify({
        "status": "unhealthy",
        "mongodb": "unavailable"
    }), 503


@app.route("/api")
def api():
    """Read data.json and return it as JSON."""
    try:
        data_file = Path(__file__).resolve().parent / "data.json"

        with data_file.open("r", encoding="utf-8") as file:
            data = json.load(file)

        return jsonify(data), 200

    except (OSError, json.JSONDecodeError) as exc:
        logger.exception("Failed to read data.json: %s", exc)

        return jsonify({
            "error": "Unable to read API data"
        }), 500


@app.route("/submit", methods=["POST"])
def submit():
    """Store student information in MongoDB."""
    try:
        if collection is None:
            return render_template(
                "index.html",
                error="MongoDB is currently unavailable."
            ), 503

        name = validate_text(
            request.form.get("name", ""),
            "Name",
            100
        )

        email = validate_text(
            request.form.get("email", ""),
            "Email",
            150
        )

        course = validate_text(
            request.form.get("course", ""),
            "Course",
            100
        )

        # Explicitly construct the document from validated strings.
        # This prevents arbitrary request data from becoming MongoDB fields.
        student = {
            "name": name,
            "email": email,
            "course": course
        }

        collection.insert_one(student)

        logger.info("Student record inserted successfully")

        return redirect("/success")

    except ValueError as exc:
        logger.warning("Student validation failed: %s", exc)

        return render_template(
            "index.html",
            error=str(exc)
        ), 400

    except PyMongoError as exc:
        logger.exception("Failed to insert student: %s", exc)

        return render_template(
            "index.html",
            error="Unable to save student information."
        ), 500

    except Exception:
        logger.exception("Unexpected error while submitting student")

        return render_template(
            "index.html",
            error="An unexpected error occurred."
        ), 500


@app.route("/api/todos", methods=["GET"])
def get_todos():
    """Return To-Do items stored in MongoDB."""
    try:
        if todo_collection is None:
            return jsonify({
                "error": "MongoDB is unavailable"
            }), 503

        # Projection prevents MongoDB's internal _id from being exposed.
        todos = list(
            todo_collection.find(
                {},
                {"_id": 0}
            )
        )

        return jsonify(todos), 200

    except PyMongoError as exc:
        logger.exception("Failed to retrieve To-Do items: %s", exc)

        return jsonify({
            "error": "Unable to retrieve To-Do items"
        }), 500


@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    """Generate identifiers and store a To-Do item in MongoDB."""
    try:
        if todo_collection is None:
            return jsonify({
                "error": "MongoDB is unavailable"
            }), 503

        item_name = validate_text(
            request.form.get("itemName", ""),
            "Item Name",
            200
        )

        item_description = validate_text(
            request.form.get("itemDescription", ""),
            "Item Description",
            1000
        )

        # Generate the next numeric Item ID.
        existing_items = todo_collection.find(
            {"itemId": {"$exists": True}},
            {"itemId": 1, "_id": 0}
        )

        item_ids = []

        for item in existing_items:
            item_id_value = item.get("itemId")

            if isinstance(item_id_value, int):
                item_ids.append(item_id_value)

        item_id = max(item_ids) + 1 if item_ids else 1

        # Generate UUID.
        item_uuid = str(uuid.uuid4())

        # Generate SHA-256 hash.
        item_hash = hashlib.sha256(
            f"{item_id}{item_uuid}{item_name}{item_description}".encode(
                "utf-8"
            )
        ).hexdigest()

        todo_item = {
            "itemId": item_id,
            "itemUuid": item_uuid,
            "itemHash": item_hash,
            "itemName": item_name,
            "itemDescription": item_description
        }

        todo_collection.insert_one(todo_item)

        logger.info(
            "To-Do item inserted successfully with itemId=%s",
            item_id
        )

        return jsonify({
            "message": "To-Do item submitted successfully",
            "itemId": item_id,
            "itemUuid": item_uuid,
            "itemHash": item_hash
        }), 201

    except ValueError as exc:
        logger.warning("To-Do validation failed: %s", exc)

        return jsonify({
            "error": str(exc)
        }), 400

    except PyMongoError as exc:
        logger.exception("Failed to insert To-Do item: %s", exc)

        return jsonify({
            "error": "Unable to save To-Do item"
        }), 500

    except Exception:
        logger.exception("Unexpected error while submitting To-Do item")

        return jsonify({
            "error": "An unexpected error occurred"
        }), 500


if __name__ == "__main__":
    app.run(debug=True)