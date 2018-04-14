from server import app
import pytest
import json

@pytest.fixture
def tester():
    return app.test_client()

@pytest.fixture
def pop_db():
    from models import reset_and_populate
    reset_and_populate()

def test_topics(tester, pop_db):
    res = tester.get('/topics', content_type='application/json')
    assert res.status_code == 200


def test_topic(tester, pop_db):
    res = tester.get('/topic/1', content_type='application/json')
    assert res.status_code == 200
    assert "error" not in json.loads(res.data)


def test_ins_ann(tester, pop_db):
    mock = {"start_paragraph": 5,
            "start_index": 10,
            "end_paragraph": 7,
            "end_index": 12,
            "body": "No this is wrong!"}

    res = tester.post("/annotations/1", data=json.dumps(mock), content_type="application/json")
    assert res.status_code == 200


def test_ins_com(tester, pop_db):
    mock = {"comment": "Funniest shit i've ever seen"}

    res = tester.post("/annotations/comment/1", data=json.dumps(mock), content_type="application/json")
    assert res.status_code == 200


def test_get_ann_meta(tester, pop_db):
    res = tester.get("/annotations/1")
    assert res.status_code == 200


def test_get_ann_text(tester, pop_db):
    res = tester.get("/annotations/1/1")
    assert res.status_code == 200

def test_put_ann_likes(tester, pop_db):
    from models import Annotation
    res = tester.post("/annotations/delta/1/true")

    assert Annotation.get_by_id(1).deltas == 1

def test_get_speeches(tester, pop_db):
    res = tester.get("/speeches/1/5")

    assert res.status_code == 200

def test_get_speech(tester, pop_db):
    res = tester.get("/speech/1")

    assert res.status_code == 200


if __name__ == '__main__':
    app.run(debug=True)
