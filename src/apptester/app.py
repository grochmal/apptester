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
    response += ['*** App Tester - Arguments ***']
    for a, v in request.args.items():
        response.append('%s: %s' % (a[:MAX_LEN], v[:MAX_LEN]))
    app.logger.info('request OK, responding')
    # Printing to STDOUT works in uWSGI but can break some
    # application servers, always use a stream logger to print.
    print('*** apptester:print to STDOUT')
    resp = make_response('\n'.join(response + ['']))
    resp.headers['Content-Type'] = 'text/plain; charset=utf-8'
    if request.args.get('raise'):
        raise RuntimeError('Boom!')
    max_age = request.args.get('max-age')
    if max_age and max_age.isdigit():
        max_age = min(int(max_age), MAX_CACHE)
        resp.headers['Cache-Control'] = 'max-age=%i' % max_age
    return resp

