from flask import Flask, render_template, request, redirect, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import json

load_dotenv()

app = Flask(__name__)

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)

database = client["studentDB"]
collection = database["students"]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api")
def api():
    with open("data.json", "r") as file:
        data = json.load(file)

    return jsonify(data)


@app.route("/submit", methods=["POST"])
def submit():
    try:
        name = request.form["name"]
        email = request.form["email"]
        course = request.form["course"]

        student = {
            "name": name,
            "email": email,
            "course": course
        }

        collection.insert_one(student)

        return redirect("/success")

    except Exception as e:
        return render_template("index.html", error=str(e))


@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)