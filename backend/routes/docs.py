from flask import jsonify, Blueprint
from models import Document
from peewee import DoesNotExist
from playhouse.shortcuts import model_to_dict


documents = Blueprint('docs', __name__)


@documents.route('/docs')
def docs():
    return jsonify({'docs': [
        {
            k:v
            for k,v
            in model_to_dict(doc).items()
            if k in ['id', 'title']
            }
        for doc in Document.select() 
        ]})


@documents.route('/doc/<docid>')
def doc(docid):
    try:
        return jsonify({
                'doc' : model_to_dict(Document.get_by_id(docid))
            })
    except DoesNotExist:
        return jsonify({
                'error' : 'doc does not exist'
            })

