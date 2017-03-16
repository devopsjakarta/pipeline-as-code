import requests
from nose.plugins.attrib import attr

def test_code():
    r = requests.get('http://127.0.0.1:8989')
    assert r.status_code == 200
