from flask import Flask, render_template, request, redirect, jsonify
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from dotenv import load_dotenv
import os
import json
import uuid
import hashlib
import logging

load_dotenv()

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# MongoDB connection
mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri)
database = client["studentDB"]

student_collection = database["students"]
todo_collection = database["todoitems"]


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# To-Do page
@app.route("/todo")
def todo():
    return render_template("todo.html")


# Success page
@app.route("/success")
def success():
    return render_template("success.html")

# Health check
@app.route("/health")
def health():
    try:
        client.admin.command("ping")
        return jsonify({"status": "healthy"}), 200
    except Exception as error:
        logger.error("MongoDB connection failed: %s", error)
        return jsonify({"status": "unhealthy"}), 500

# API route - return data from data.json
@app.route("/api")
def api():
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    return jsonify(data)


# Submit student information
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    course = request.form.get("course", "").strip()

    if not name or not email or not course:
        return jsonify({"error": "All fields are required"}),400

    student = {
        "name": name,
        "email": email,
        "course": course
    }

    try:
        student_collection.insert_one(student)
        return redirect("/success")
    except PyMongoError as error:
        logger.error("Error saving student: %s", error)
        return jsonify({"error": "Could not save student"}),500


# Get all To-Do items
@app.route("/api/todos")
def get_todos():
    try:
        todos = list(todo_collection.find({}, {"_id": 0}))
        return jsonify(todos)
    except PyMongoError as error:
        logger.error("Error getting To-Do items: %s", error)
        return jsonify({"error": "Could not get To-Do items"}),500


@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    item_name = request.form.get("itemName", "").strip()
    item_description = request.form.get("itemDescription", "").strip()

    if not item_name or not item_description:
        return jsonify({"error": "Item name and description are required"}), 400

    if len(item_name) > 200 or len(item_description) > 1000:
        return jsonify({"error": "Input is too long"}), 400

    try:
        # Generate Item ID
        existing_items = todo_collection.find({}, {"itemId": 1, "_id": 0})

        item_ids = []

        for item in existing_items:
            if isinstance(item.get("itemId"), int):
                item_ids.append(item["itemId"])

        if item_ids:
            item_id = max(item_ids) + 1
        else:
            item_id = 1

        # Generate UUID
        item_uuid = str(uuid.uuid4())

        # Generate SHA-256 hash
        item_hash = hashlib.sha256(
            f"{item_id}{item_uuid}{item_name}{item_description}".encode("utf-8")
        ).hexdigest()

        todo_item = {
            "itemId": item_id,
            "itemUuid": item_uuid,
            "itemHash": item_hash,
            "itemName": item_name,
            "itemDescription": item_description
        }

        todo_collection.insert_one(todo_item)

        return jsonify({
            "message": "To-Do item submitted successfully",
            "itemId": item_id,
            "itemUuid": item_uuid,
            "itemHash": item_hash
        }), 201

    except PyMongoError as error:
        logger.error("Error saving To-Do item: %s", error)
        return jsonify({"error": "Could not save To-Do item"}), 500


if __name__ == "__main__":
    app.run(debug=True)