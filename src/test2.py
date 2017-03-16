import requests
from nose.plugins.attrib import attr

def test_code():
    r = requests.get('http://127.0.0.1:8000')
    assert r.status_code == 200
