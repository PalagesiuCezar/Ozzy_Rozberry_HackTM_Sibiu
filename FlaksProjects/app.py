import os

from flask import request, session, jsonify
import base64
import pickle
import subprocess

import requests
from flask import request
from flask_api import FlaskAPI


def case_rotire(query):
    rotire = 0
    set1 = 0

    caseUNU = ['bottle', 'toilet', 'pet', 'nipple']
    for i in caseUNU:
        if i in query:
            rotire = 1
            set1 = 1

    if set1 != 1:
        caseDOI = ['can', 'crate', 'aluminium', 'oil', 'filter']
        for i in caseDOI:
            if i in query:
                rotire = 2
                set1 = 1

    if set1 != 1:
        caseTREI = ['glass', 'bottle', 'water', 'beer', 'juice']
        for i in caseTREI:
            if i in query:
                rotire = 3

    if set1 != 1:
        casePATRU = ['bag', 'cardboard']
        for i in casePATRU:
            if i in query:
                rotire = 4

    return rotire


def image_dumps(data):
    with open('recicle.jpeg', 'wb') as imgFile:
        image = imgFile.write(base64.b64decode(data))

    subprocess.call("python3 classify_image.py --image_file {}".format('recicle.jpeg'), shell=True)

    with open('data.txt', 'rb') as data:
        query = pickle.load(data)
    query = str(query)

    dap = case_rotire(query)
    print(dap)
    return dap


app = FlaskAPI(__name__)
app.secret_key = "sdfsd "


@app.route('/', methods=['GET', 'PUT'])
def image():
    if request.method == 'GET':
        data = requests.get("http://localhost:6666/").content
        query = image_dumps(data)
        resp = jsonify({'imaginea': data,
                'compartimentul ': query
                })
        resp.set_cookie("query", str(query))
        return resp

    # return redirect(url_for('send_data'))


@app.route('/12', methods=['GET', 'PUT'])
def send_data():
    # query = request.args.get('query')
    # query = request.form.get('query')
    query = int(request.cookies.get("query", None))
    if request.method == 'GET':
        return {'compartimentuL': query}


if __name__ == '__main__':
    app.run(debug=True, host='192.168.88.147', port=8080)
