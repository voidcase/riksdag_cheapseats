from flask import Flask, jsonify
from models import Document
from playhouse.shortcuts import model_to_dict

app = Flask(__name__)

# returns json with all docs
@app.route('/docs')
def docs():
    return jsonify({'docs':[
        {
            k:v
            for k,v
            in model_to_dict(doc).items()
            if k in ['id', 'title']
            }
        for doc in Document.select() 
        ]})
