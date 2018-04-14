from flask import jsonify, Blueprint
from models import Document
from peewee import DoesNotExist
from playhouse.shortcuts import model_to_dict


topics_bp = Blueprint('topics', __name__)


@topics_bp.route('/topic')
def topics():
    return jsonify({'topic': [
        {
            k:v
            for k,v
            in model_to_dict(doc).items()
            if k in ['id', 'title']
            }
        for doc in Document.select() 
        ]})


@topics_bp.route('/topic/<topic_id>')
def topic(topic_id):
    try:
        return jsonify({
                'doc' : model_to_dict(Document.get_by_id(topic_id))
            })
    except DoesNotExist:
        return jsonify({
                'error' : 'doc does not exist'
            })

