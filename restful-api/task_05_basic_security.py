#!/usr/bin/python3
"""
API Security and Authentication: Basic Auth and JWT Implementation.
Includes role-based access control (RBAC).
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt
)


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Change in production
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# In-memory user data
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


@auth.verify_password
def verify_password(username, password):
    """Verifies basic auth credentials."""
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username
    return None


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Route protected by Basic Authentication."""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """Authenticates user and returns a JWT token."""
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        # Store role in the token claims
        additional_claims = {"role": user['role']}
        access_token = create_access_token(
            identity=username,
            additional_claims=additional_claims
        )
        return jsonify(access_token=access_token)

    return jsonify({"error": "Bad username or password"}), 401


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Route protected by JWT Authentication."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Route protected by JWT with Role-based Access Control (Admin only)."""
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


# Custom JWT error handlers to ensure 401 status code
@jwt.unauthorized_loader
def my_unauthorized_callback(msg):
    return jsonify({"error": msg}), 401


@jwt.invalid_token_loader
def my_invalid_token_callback(msg):
    return jsonify({"error": msg}), 401


@jwt.expired_token_loader
def my_expired_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
