#!/usr/bin/env python


import logging
from flask import Flask, request, make_response
from flask.logging import default_handler


app = Flask(__name__)
app.logger.setLevel(logging.INFO)
default_handler.setFormatter(logging.Formatter(
 '*** apptester:%(asctime)s:%(levelname)s:%(filename)s:%(lineno)d:%(message)s'
))
MAX_LEN = 1024  # prevent overload attacks
MAX_CACHE = 30


@app.route('/apptester')
def apptester():
    response = ['*** App Tester - Request Headers ***']
    for h, c in request.headers.items():
        response.append('%s: %s' % (h[:MAX_LEN], c[:MAX_LEN]))
    response.append('*** App Tester - Arguments ***')
    for k, v in request.args.items():
        response.append('%s: %s' % (k[:MAX_LEN], v[:MAX_LEN]))
    response.append('*** App Tester - URL parameters ***')
    response.append('URL: %s' % request.url)
    response.append('DATE: %s' % request.date)
    response.append('ENDPOINT: %s' % request.endpoint)
    response.append('HOST: %s' % request.host)
    response.append('PATH: %s' % request.path)
    response.append('METHOD: %s' % request.method)
    response.append('REFERRER: %s' % request.referrer)
    response.append('REMOTE ADDR: %s' % request.remote_addr)
    response.append('SCHEME: %s' % request.scheme)
    response.append('HTTPS: %s' % request.is_secure)
    response.append('MULTIPROCESS: %s' % request.is_multiprocess)
    response.append('MULTITHREAD: %s' % request.is_multithread)
    response.append('RUN ONCE: %s' % request.is_run_once)
    # deprecated, see https://github.com/pallets/flask/issues/2549
    #response.append('XHR: %s' % request.is_xhr)
    response.append('USER AGENT: %s' % request.user_agent)
    response.append('*** App Tester - Cookies ***')
    print(request.cookies)
    for k, v in request.cookies.items():
        response.append('%s: %s' % (k[:MAX_LEN], v[:MAX_LEN]))
    response.append('*** App Tester - Environment ***')
    for h, c in request.environ.items():
        response.append('%s: %s' % (h[:MAX_LEN], c))
    app.logger.info('request OK, responding')
    # Printing to STDOUT works in uWSGI but can break some
    # application servers, always use a stream logger to print.
    print('*** apptester:print to STDOUT')
    resp = make_response('\n'.join(response + ['']))
    resp.headers['Content-Type'] = 'text/plain; charset=utf-8'
    # play exceptions safe, tests will come from localhost
    addr = request.remote_addr
    if request.args.get('raise') and '127.0.0.1' == addr:
        raise RuntimeError('Boom!')
    max_age = request.args.get('max-age')
    if max_age and max_age.isdigit():
        max_age = min(int(max_age), MAX_CACHE)
        resp.headers['Cache-Control'] = 'max-age=%i' % max_age
    user = request.cookies.get('userid')
    if user:
        resp.headers['Cache-Control'] = 'no-cache'
    return resp

