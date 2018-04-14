from server import app
import pytest
import json


@pytest.fixture
def tester():
    return app.test_client()

def test_docs(tester):
    res = tester.get('/docs', content_type='application/json')
    assert res.status_code == 200

def test_doc(tester):
    res = tester.get('/doc/1', content_type='application/json')
    assert res.status_code == 200
    assert "error" not in json.loads(res.data)

if __name__ == '__main__':
    app.run(debug=True)
