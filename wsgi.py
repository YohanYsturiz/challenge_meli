from flask import Flask

from routes.items_routes import items
from settings.db_connection import engine
from settings.base import Config

db = engine

app = Flask(__name__)

app.register_blueprint(items)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=Config.DEBUG)
