from server import app
import pytest


@pytest.fixture
def tester():
    return app.test_client()

def test_docs(tester):
    res = tester.get('/docs', content_type='application/json')
    assert res.status_code == 200

if __name__ == '__main__':
    app.run(debug=True)
