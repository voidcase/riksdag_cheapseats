<<<<<<< HEAD
from flask import Flask, jsonify
from models import Topic
from peewee import DoesNotExist
from playhouse.shortcuts import model_to_dict
from routes.docs import documents

app = Flask(__name__)
app.register_blueprint(documents)

# returns json with all docs
if __name__ == '__main__':
    app.run(debug=True)
