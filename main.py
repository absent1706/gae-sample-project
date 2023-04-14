# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_flex_quickstart]
from pprint import pformat

from flask import Flask, request
import logging
import os

# from google.cloud import error_reporting
from dotenv import load_dotenv

logging.basicConfig(level=logging.DEBUG)
load_dotenv()

app = Flask(__name__)

# error_reporting_client = error_reporting.Client()


def _request_info():
    return \
    f'<pre>' \
    f'Request method: {request.method} \n' \
    f'Request URL: {request.url} \n \n' \
    f'Request headers: \n {request.headers} \n' \
    f'Request data: {request.get_data()} \n' \
    f'</pre>'


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print('PRINT')
    logging.info('this is log entry')

    urls = [rule.rule for rule in app.url_map.iter_rules()]
    return f'Hello World from version {os.getenv("GAE_VERSION")}! \n \n' \
           f'{_request_info()}' \
           f'\n ======= URLs available: ========= \n' \
           f' \n <pre>{pformat(urls)}</pre> \n'


@app.route('/public/route1')
def public_route1():
    return f'public route 1 \n {_request_info()}'


@app.route('/public/route2')
def public_route2():
    return f'public route 2 \n {_request_info()}'


@app.route('/private-route1')
def private_route1():
    return f'private route 1 \n {_request_info()}'


@app.route('/private-route2')
def private_route2():
    return f'private route 2 \n {_request_info()}'


@app.route('/500')
def error_path():
    raise ValueError('another test error')


@app.route('/error2')
def error2_path():
    raise NameError('test NameError')


@app.errorhandler(404)
def resource_not_found(e):
    urls = [rule.rule for rule in app.url_map.iter_rules()]
    response = f'{e} \n {_request_info()}' \
               f'\n ======= URLs available: ========= \n' \
               f' \n <pre>{pformat(urls)}</pre> \n'
    return response, 404


@app.errorhandler(Exception)
def handler(exception):
    # error_reporting_client.report_exception()
    logging.exception(exception)
    raise


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app.
    app.run(host='0.0.0.0', port=8081, debug=True)
# [END gae_flex_quickstart]
