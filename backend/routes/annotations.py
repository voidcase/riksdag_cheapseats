from flask import Blueprint, request, Response, abort
from sys import stderr
import json
from models import Annotation
from peewee import IntegrityError


annotaions_bp = Blueprint('annotations', __name__)


@annotaions_bp.route("/annotations/<topic_id>", methods=["POST"])
def ins_ann(topic_id):
    """
    Request Includes annotations and corresponding text.

    Should insert annotation.

    params:

    """
    annotations_text = None
    try:
        data = json.loads(request.data)
        ctrl.add_annotation(topic_id, data)
    except json.JSONDecodeError as e:
        stderr.write("Unable to parse JSON request from /annotations/ \
                      reason: {}".format(str(e)))
    except IntegrityError as e:
        abort(400)

    """Do something with annotations."""
    return Response("Hi", status=200, mimetype="text/plain")


@annotaions_bp.route("/annotations/<topic_id>/<annotation_id>", methods=["POST"])
def ins_com(topic_id, annotation_id):
    """Insert comment on annotation."""
    ann_comm = None
    try:
        ann_comm = json.loads(request.data)
    except json.JSONDecodeError as e:
        stderr.write("Unable to parse JSON request when attempting to \
                      add comment, reason: {}".format(str(e)))

    return Response("Hello", status=200, mimetype="text/plain")


@annotaions_bp.route("/annotations/<topic_id>", methods=["GET"])
def get_ann_meta(topic_id):
    """Return annotation meta data."""
    return Response("Totally a annotation", status=200, mimetype="text/plain")


@annotaions_bp.route("/annotations/<topic_id>/<annotation_id>", methods=["GET"])
def get_ann_text(topic_id, annotation_id):
    """Get text for annotation and comments."""
    return Response("Totally text and comments", status=200, mimetype="text/plain")






