from flask import Blueprint, request, Response, abort
from sys import stderr
import json
from models import Annotation, Comment
from peewee import IntegrityError


annotations_bp = Blueprint('annotations', __name__)


@annotations_bp.route("/annotations/<topic_id>", methods=["POST"])
def ins_ann(topic_id):
    """
    Request Includes annotations and corresponding text.

    Should insert annotation.

    params:

    """
    try:
        data = json.loads(request.data)
        ann = Annotation.create(
            parent=topic_id,
            start_index=data['start_index'],
            end_index=data['end_index'],
            start_paragraph=data['start_paragraph'],
            end_paragraph=data['end_paragraph'],
            body=data['body'],
            deltas=0)
        ann.save()
    except json.JSONDecodeError as e:
        stderr.write("Unable to parse JSON request from /annotations/ \
                      reason: {}".format(str(e)))
    except IntegrityError as e:
        stderr.write("Integrity error when inserting annotation: {}".format(str(e)))
        abort(400)

    """Do something with annotations."""
    return Response("Hi", status=200, mimetype="text/plain")


@annotations_bp.route("/annotations/comment/<annotation_id>", methods=["POST"])
def ins_com(annotation_id):
    """Insert comment on annotation."""
    ann_comm = None
    try:
        data = json.loads(request.data)
        ann = Annotation.get_by_id(annotation_id)
        comm = Comment(
            parent=annotation_id,
            body=data['comment'],
            deltas = 0
        )
        comm.save()
    except json.JSONDecodeError as e:
        stderr.write("Unable to parse JSON request when attempting to \
                      add comment, reason: {}".format(str(e)))

    return Response("Hello", status=200, mimetype="text/plain")

@annotations_bp.route("/annotations/delta/<annotation_id>/<up_or_down>", methods=["POST"])
def mod_ann_delta(annotation_id, up_or_down):
    """Add a delta to an annotation or comment"""
    try:
        ann = Annotation.get_by_id(annotation_id)
        if up_or_down == 'true':
            ann.deltas += 1
        else:
            if ann.deltas > 0:
                ann.deltas -= 1
        ann.save()
    except DoesNotExist as e:
        stderr.write("Unable to find annotation_id in db: {}").format(str(e))
    
    return Response("Yo", status=200, mimetype="text/plain")

@annotations_bp.route("/annotations/<topic_id>", methods=["GET"])
def get_ann_meta(topic_id):
    """Return annotation meta data."""
    return Response("Totally a annotation", status=200, mimetype="text/plain")

@annotations_bp.route("/annotations/<topic_id>/<annotation_id>", methods=["GET"])
def get_ann_text(topic_id, annotation_id):
    """Get text for annotation and comments."""
    return Response("Totally text and comments", status=200, mimetype="text/plain")






