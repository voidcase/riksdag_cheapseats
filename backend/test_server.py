from server import app
import pytest
import json


@pytest.fixture
def tester():
    return app.test_client()

def test_topics(tester):
    res = tester.get('/topics', content_type='application/json')
    assert res.status_code == 200


def test_topic(tester):
    res = tester.get('/topic/1', content_type='application/json')
    assert res.status_code == 200
    assert "error" not in json.loads(res.data)


if __name__ == '__main__':
    app.run(debug=True)
