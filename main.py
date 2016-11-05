# [START app]
import logging

from flask import Flask, send_file, send_from_directory, make_response
from flask_cors import CORS, cross_origin

import sfg_termination

app = Flask(__name__)

# enable cors (dev only!!)
CORS(app)

@app.route('/api/document/termination', methods=['POST'])
def ct():

    pdf = sfg_termination.create_termination(request.data)

    response = make_response(pdf)
    #response.headers['Content-Disposition'] = "attachment; filename='sakulaci.pdf"
    response.headers['Content-Disposition'] = 'inline; filename=%s.pdf' % 'yourfilename'
    response.mimetype = 'text/html'
    return response

@app.route('/')
def index():
    return send_file('node/build/index.html')

@app.route('/<path:path>')
def send_angular(path):
    return send_from_directory('node/build', path)

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occured during request')
    return 'Internal Server Error', 500

# [END app]
