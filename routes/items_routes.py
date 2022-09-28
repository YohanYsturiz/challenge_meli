import json
from flask import Blueprint, jsonify, request
from apps.items.services.items import read_file

items = Blueprint('items', __name__)

@items.get("/api/health")
def status_get():
    return jsonify({"message": "ok"})


@items.post("/api/upload")
def upload_file():
    file = request.files["the_file"]
    params = request.form["params"]

    items_count = read_file(file, json.loads(params))

    return jsonify({"message": "success", "items_count": items_count})