#!/usr/bin/env python


import pytest
from apptester import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_req(client):
    resp = client.get('/apptester')
    assert resp.status_code == 200


def test_head(client):
    resp = client.head('/apptester')
    assert resp.status_code == 200


def test_no_root(client):
    resp = client.get('/')
    assert resp.status_code == 404


def test_header(client):
    resp = client.get('/apptester', headers={'X-Request-Id': 'blah'})
    assert b'X-Request-Id: blah' in resp.data


def test_xhr(client):
    resp = client.get('/apptester',
                      headers={'X-Requested-With': 'XMLHttpRequest'})
    assert b'XHR: True' in resp.data


def test_cookie(client):
    resp = client.get('/apptester',
                      headers={'Cookie': 'userid=13; sessionid=3'})
    assert b'userid: 13' in resp.data


def test_environment(client):
    resp = client.get('/apptester')
    assert b'wsgi.errors' in resp.data


def test_argument(client):
    resp = client.get('/apptester?pink-parfait')
    assert b'pink-parfait' in resp.data


def test_cache(client):
    resp = client.get('/apptester?max-age=12')
    assert resp.headers['Cache-Control'] == 'max-age=12'


def test_cache_limit(client):
    resp = client.get('/apptester?max-age=45')
    assert resp.headers['Cache-Control'] == 'max-age=30'


def test_header_limit(client):
    resp = client.get('/apptester', headers={'X-Request-Id': '3' * 2048})
    assert b'X-Request-Id: ' + b'3' * 1024 in resp.data


def test_raise(client):
    with pytest.raises(RuntimeError):
        client.get('/apptester?raise=1')

