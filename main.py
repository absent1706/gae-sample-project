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
from flask import Flask
import logging
from google.oauth2 import service_account
from google.cloud import error_reporting
from dotenv import load_dotenv

logging.basicConfig(level=logging.DEBUG)
load_dotenv()

app = Flask(__name__)

error_reporting_client = error_reporting.Client()


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print('PRINT')
    logging.info('this is log entry')
    return 'Hello World!'


@app.route('/500')
def error_path():
    raise ValueError('another test error')


@app.route('/error2')
def error2_path():
    raise NameError('test NameError')


@app.errorhandler(Exception)
def handler(exception):
    error_reporting_client.report_exception()
    raise


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app.
    app.run(host='0.0.0.0', port=8080, debug=True)
# [END gae_flex_quickstart]
