"""
Server file of flask
"""
from flask import Flask
from flask_cors import CORS

from coMakeIT import coMakeIT_routes_blueprint

app = Flask(__name__)
CORS(app)

app.register_blueprint(coMakeIT_routes_blueprint)

if __name__ == '__main__':
    app.run(host='localhost', port=9002)

