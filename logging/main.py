from flask import Flask, render_template

from test_service import ciao
import logging
from flask import has_request_context, request
from flask.logging import default_handler

app = Flask(__name__)

class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None

        return super().format(record)

formatter = RequestFormatter(
    '[%(asctime)s] %(remote_addr)s requested %(url)s\n'
    '%(levelname)s in %(module)s: %(message)s'
)
default_handler.setFormatter(formatter)

@app.route('/')
def index():
    app.logger.info("Ciao")
    ciao()
    return 'Flask Template', 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 