from flask import Blueprint, request
from sys import stderr
import json


annotaions_bp = Blueprint('annotations', __name__)


@annotaions_bp.route("/annotations/<topic_id>", methods=["POST"])
def ins_ann(topic_id):
    """Request Includes annotations and corresponding text."""
    annotations_text = None
    try:
        annotations_text = json.loads(request.data)
    except json.JSONDecodeError as e:
        stderr.write("Unable to parse JSON request from /annotations/ \
                      reason: {}".format(str(e)))

    """Do something with annotations."""
    print(annotations_text)
    return "Hi"


@annotaions_bp.route("/annotations/<topic_id>/<annotation_id>", methods=["POST"])
def ins_com(topic_id, ann_id):
    """Insert comment on annotation."""
    ann_comm = None
    try:
        ann_comm = json.loads(request.data)
    except json.JSONDecodeError as e:
        stderr.write("Unable to parse JSON request when attempting to \
                      add comment, reason: {}".format(str(e)))

    print(ann_comm)



@annotaions_bp.route("/annotations/<topic_id>", methods=["GET"])
def get_ann_meta(topic_id):
    """Return annotation meta data."""
    return "Totally a annotation"


@annotaions_bp.route("/annotations/<topic_id>/<annotation_id>", methods=["GET"])
def get_ann_text(topic_id, ann_id):
    """Get text for annotation and comments."""
    return "Totally text and comments"






