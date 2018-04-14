from flask import Flask, jsonify
from models import Topic
from peewee import DoesNotExist
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
        for doc in Topic.select()
        ]})


@app.route('/doc/<topid>')
def doc(topid):
    try:
        return jsonify({
                'doc' : model_to_dict(Topic.get_by_id(topid))
            })
    except DoesNotExist:
        return jsonify({
                'error' : 'doc does not exist'
            })

if __name__ == '__main__':
    app.run(debug=True)
