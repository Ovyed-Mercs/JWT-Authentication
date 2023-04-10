"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


api = Blueprint('api', __name__)


@api.route('/users', methods=['GET'])
def get_users():
    users= User.query.all()
    serialized_users=[]
    for user in users:
        serialized_users.append(user.serialize())

    response_body = {
        "message": "Here's the List of Users",
        "users": serialized_users
    }

    return jsonify(response_body), 200




@api.route('/user', methods=['POST'])
def add_user():
    email= request.json.get("email")
    password= request.json.get("password")
    if email is None:
        return "Provide a valid email", 400
    if password is None:
        return "Enter a password", 400
    
    check_user= User.query.filter_by(email=email).first()
    if check_user:
        return "Email already taken", 409

    user= User(email=email,password=password, is_active=True)
    db.session.add(user)
    db.session.commit()

    response_body = {
        "message": "Successfully registered",
        "users": user.serialize()
    }

    return jsonify(response_body), 200

@api.route('/login', methods=['POST'])
def login_user():
    email= request.json.get("email", None)
    password= request.json.get("password", None)
    user= User.query.filter_by(email=email, password=password).first()
    
    if user is None:
        return jsonify({"message":"bad username or password"}), 401
    
    return jsonify(response_body), 200