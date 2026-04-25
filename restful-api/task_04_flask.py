#!/usr/bin/python3
"""
A simple API built with Flask.
Provides endpoints for status, user data, and adding new users.
"""
from flask import Flask, jsonify, request


app = Flask(__name__)

# In-memory dictionary to store users
users = {}


@app.route("/")
def home():
    """Returns a welcome message for the root URL."""
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """Returns the status of the API."""
    return "OK"


@app.route("/data")
def get_data():
    """Returns a list of all usernames stored in the API."""
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    """Returns the full object for a specific username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Adds a new user to the users dictionary with validation."""
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
