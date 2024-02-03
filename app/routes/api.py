from flask import Blueprint, jsonify


api_bp = Blueprint("api", __name__)


@api_bp.route("/products")
def get_products():
    pass