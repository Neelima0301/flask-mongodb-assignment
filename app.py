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
todo_collection = database["todoitems"]


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/todo")
def todo():
    return render_template("todo.html")

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

@app.route("/api/todos", methods=["GET"])
def get_todos():
    todos = list(todo_collection.find({}, {"_id": 0}))
    return jsonify(todos)

@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    try:
        item_name = request.form["itemName"]
        item_description = request.form["itemDescription"]

        todo_item = {
            "itemName": item_name,
            "itemDescription": item_description
        }

        todo_collection.insert_one(todo_item)

        return "To-Do item submitted successfully"

    except Exception as e:
        return str(e), 500
    
if __name__ == "__main__":
    app.run(debug=True)

    