# [START app]
import logging

from flask import Flask, send_file, send_from_directory, make_response

import sfg_termination

app = Flask(__name__)

@app.route('/api/document/termination', methods=['GET'])
def create_termination():
#    name = request.form['name']
#    email = request.form['email']
#    site = request.form['site_url']
#    comments = request.form['comments']

    pdf = sfg_termination.create_termination()

    response = make_response(pdf)
    response.headers['Content-Disposition'] = "attachment; filename='sakulaci.pdf"
    response.mimetype = 'application/pdf'
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
