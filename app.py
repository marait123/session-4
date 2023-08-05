from flask import Flask, jsonify
from itsdangerous import json

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify(greeting="welcome 1 121 1", code=123)


if __name__ == "__main__":
    app.run(host="0.0.0.0",  debug=True)

# E:\udacity\sessions\session 4\codes\app.py
# build the aimge
#  docker build -t  flaskimage:3 .
# running docker container
#  docker run --name flask_app -p 5000:5000 --mount type=bind,source="$(pwd)",target=/app -d flaskimage:3
#  docker run --name flask_app -p 5000:5000 -d flaskimage:3
