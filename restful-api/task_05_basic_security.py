#!/usr/bin/python3
"""Simple RESTful API using Flask"""
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_httpauth import HTTPBasicAuth

from flask_jwt_extended import JWTManager, jwt_required
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'secretkey'
auth = HTTPBasicAuth()
jwt = JWTManager(app)
users = {
    "user1": {
         "username": "user1",
         "password": generate_password_hash("password"),
         "role": "user"
    },
    "admin1": {
         "username": "admin1",
         "password": generate_password_hash("password"),
         "role": "admin"
    }
}


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Basic protected endpoint"""
    return "Basic Auth: Access Granted"


@auth.verify_password
def verify_password(username, password):
    """Verify password callback"""
    if username in users:
        if check_password_hash(users[username]["password"], password):
            return users[username]


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """JWT protected endpoint"""
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Admin only endpoint"""
    current_user = get_jwt_identity()
    if current_user["role"] == "admin":
        return "Admin Access: Granted", 200
    return jsonify({"error": "Admin access required"}), 403


@app.route('/login', methods=['POST'])
def login():
    """Login endpoint"""
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    if username not in users:
        return jsonify({"error": "Invalid username"}), 400

    if not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Invalid password"}), 401

    access_token = create_access_token(identity=users[username])
    return jsonify(access_token=access_token), 200


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run()
