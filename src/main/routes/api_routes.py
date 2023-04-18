from flask import Blueprint, jsonify, request
from src.main.adapter import flask_adapter
from src.main.composer import login_user_compose,register_composite
from src.main.composer import find_user_composite

api_routes_bp = Blueprint("api_routes",__name__)

@api_routes_bp.route("/api/jwt/create/",methods=["POST"])
def login():

    message = {}
    response = flask_adapter(request=request, api_route=login_user_compose())
    if response.status_code < 300:
        return jsonify(response.body), response.status_code
    
    return jsonify(
        {
        "error": response.body,
        }
    ), response.status_code

@api_routes_bp.route("/api/auth/", methods=["POST"])
def register():
    response = flask_adapter(request=request, api_route=register_composite())
    if response.status_code < 300:
        return jsonify(response.body), response.status_code
    
    return jsonify(
        {
        "error": response.body,
        }
    ), response.status_code


@api_routes_bp.route("/api/auth/me/",methods= ["PATCH","GET"])
def me():
    response = flask_adapter(request, api_route=find_user_composite())
    if response.status_code < 300:
        return jsonify({"user":response.body})

    return jsonify({"erro":response.body}), response.status_code
    

