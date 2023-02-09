from flask import Blueprint, jsonify, request


api_routes_bp = Blueprint("api_routes",__name__)

@api_routes_bp.route("/")
def home():
    return "<h1> testando </h1>"