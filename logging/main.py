from flask import Flask, render_template

from test_service import ciao
import logging
from flask import has_request_context, request
from flask.logging import default_handler
import uuid

app = Flask(__name__)

class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.path = request.path
            record.id = request.id
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.path = None
            record.id = None
            record.url = None
            record.remote_addr = None

        return super().format(record)

# formatter = RequestFormatter(
#     '[%(asctime)s] %(remote_addr)s requested %(url)s\n'
#     '%(levelname)s in %(module)s: %(message)s\n'
#     '%(request_hash)s'
# )
formatter = RequestFormatter(
    '[%(asctime)s - id: %(id)s] %(levelname)s in %(module)s - path %(path)s: %(message)s'
)
default_handler.setFormatter(formatter)


@app.before_request
def before_request():
    request.id = str(uuid.uuid4())


@app.route('/')
def index():
    app.logger.info("Ciao")
    ciao()
    return 'Flask Template', 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 