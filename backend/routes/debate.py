from flask import jsonify, Blueprint
from models import Debate, Speech
from peewee import DoesNotExist
from playhouse.shortcuts import model_to_dict


debate_bp = Blueprint('debate', __name__)


@debate_bp.route('/speeches/<debate_id>/<count>')
def speeches(debate_id, count):
    speeches = Speech.select().order_by(Speech.nr).where(Speech.debate_id == debate_id).limit(int(count))
    data = [model_to_dict(sp) for sp in speeches]
    return jsonify(data)


@debate_bp.route('/speech/<speech_id>')
def speech(speech_id):
    try:
        data = Speech.get_by_id(speech_id)
        return jsonify(model_to_dict(data))
    except DoesNotExist:
        return jsonify({
                'error' : 'doc does not exist'
            })

