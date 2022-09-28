import os

from flask import Flask
from routes.items_routes import items
from settings.db_connection import engine

db = engine

app = Flask(__name__)

app.register_blueprint(items)

if __name__ == "__main__":
    app.run(debug=True)