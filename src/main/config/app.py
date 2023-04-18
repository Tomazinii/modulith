from flask import Flask
from flask_cors import CORS
from src.main.routes import api_routes_bp
from datetime import datetime
import redis

app = Flask(__name__)
CORS(app)

redis_con = redis.Redis(host="localhost", port=6379, db=0)

@app.route("/", methods=["GET"])
def home():
    if redis_con.get("dt") == None:
        redis_con.set("dt", str(datetime.now()))
    return redis_con.get("dt")

app.register_blueprint(api_routes_bp)