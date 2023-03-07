from flask import Blueprint, jsonify, request
from src.main.adapter import flask_adapter
from src.main.composer import login_user_compose


api_routes_bp = Blueprint("api_routes",__name__)


@api_routes_bp.route("/api/jwt/create/",methods=["POST","GET"])
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