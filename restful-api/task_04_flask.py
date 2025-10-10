#!/usr/bin/python3
#!/usr/bin/python3
"""
Simple Flask API for user management.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)


users = {}


@app.route('/')
def home():
    """Return welcome message."""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """Return list of usernames."""
    return jsonify(list(users.keys())), 200


@app.route('/status')
def status():
    """Return status message."""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Return user info or error if not found."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user from JSON data."""
    data = request.get_json()

    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data['username']
    users[username] = {
        "username": username,
        "name": data.get('name', ''),
        "age": data.get('age', ''),
        "city": data.get('city', '')
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == '__main__':
    """Run the Flask app."""
    app.run(debug=True)
