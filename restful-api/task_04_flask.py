#!/usr/bin/python3
"""Simple RESTful API using Flask"""
from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)
users = {}


@app.route('/')
def home():
    """Home endpoint"""
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    """Data endpoint"""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """Status endpoint"""
    return "OK"


@app.route('/users/<username>')
def user(username):
    """User endpoint"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Add user endpoint"""
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    if "username" not in data or not data["username"]:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    user_data = {
        "username": data["username"],
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }
    users[username] = user_data

    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201


if __name__ == "__main__":
    app.run()
