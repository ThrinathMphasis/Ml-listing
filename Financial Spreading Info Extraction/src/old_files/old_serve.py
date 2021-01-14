#!/usr/bin/env python3

from flask_cors import CORS
import requests
import traceback

from flask import Flask, request, Response,jsonify
from io import StringIO
from pages import get_pages

import os
import pandas as pd

import numpy as np

app = Flask(__name__)
CORS(app)

@app.route('/ping', methods=['GET'])
def check():
    return jsonify({"status":"Api is working"}),200
        
@app.route('/invocations', methods=['POST'])
def upload():
    if 'inputfiles' not in request.files:
        print(request.headers)
        print("error")
        print(request.files)
        return jsonify({'error': 'no file'}), 400       
    else:
        input_dir = "../input"
        if not os.path.exists(input_dir):
            os.makedirs(input_dir)
        print(request)
        print("successful")
        f = request.files['inputfiles']
        filename=f.filename
        f.save(os.path.join("../input",filename))
        
        if filename.endswith('.pdf'):
            filepath=os.path.join("../input",filename)
            print(filepath)
    try:
        
        #filepath = "../input/2014 - Annual Report - Panalpina Welttransport Holding AG.pdf"
        Dict = get_pages(filepath)
        
        return jsonify(Dict)
    except Exception as e:
        return Response(response=e,status=205,mimetype='text/plain')


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000,debug=True)