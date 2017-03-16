import requests
from nose.plugins.attrib import attr
import sys

port = sys.argv[1]

def test_code():
    r = requests.get('http://127.0.0.1:8000')
    assert r.status_code == 200
