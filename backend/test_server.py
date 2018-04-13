from server import app
import pytest


@pytest.fixture
def tester():
    return app.test_client()

@pytest.mark.parametrize('route', [
    ('/docs', 200),
    ])
def test_public_get_status_ok(tester, route):
    res = tester.get('/',content_type='html/text')
    assert res.status_code == 200

if __name__ == '__main__':
    app.run(debug=True)
