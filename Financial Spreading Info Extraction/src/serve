#!/usr/bin/env python3

import flask
from flask import Flask, request
from pages import get_pages
from extract_from_zip import extract
import os, shutil
import json
import os.path
from os import path

os.environ['TIKA_SERVER_JAR'] = "/opt/program/tika/tika-server-1.9.jar"
print(os.environ.get("TIKA_SERVER_JAR"))

class modelError(Exception):
    pass

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    """Determine if the container is working and healthy. In this sample container, we declare
    it healthy if we can load the model successfully."""
    status = 200 
    return flask.Response(response='\n', status=status, mimetype='application/json')
        
@app.route('/invocations', methods=['POST'])
def upload():
    #### Takes input as .zip file
    if request.content_type == 'application/zip':
        data_file = request.data
        with open('Input.zip','wb') as f:
            f.write(data_file)
    else:
        return flask.Response(response="Input file is not utf-8 encoded pdf in a zip file. please upload utf-8 encoded file", status=500, mimetype='text/plain')
    
    try:
        # Input has config as well as input data. following function extracts both
        filepath = extract('Input.zip')
    except Exception as e:
        return flask.Response(response="Give name of the zip file as Input.zip which contain a file named Input: where the .pdf is present ",status=510,mimetype='text/plain')
    try:
        
        if path.exists("../../tmp/tika-server.log"):
            
            os.remove("../../tmp/tika-server.log")
            shutil.copy("/opt/program/tmp/tika-server.log", "../../tmp/tika-server.log")
        else:
            shutil.copy("/opt/program/tmp/tika-server.log", "../../tmp/tika-server.log")
        
        if path.exists("../../tmp/tika-server.jar.md5"):
            os.remove("../../tmp/tika-server.jar.md5")
            shutil.copy("/opt/program/tmp/tika-server.jar.md5", "../../tmp/tika-server.jar.md5")
        else:
            shutil.copy("/opt/program/tmp/tika-server.jar.md5", "../../tmp/tika-server.jar.md5")
        
        if path.exists("../../tmp/tika-server.jar"):
            os.remove("../../tmp/tika-server.jar")
            shutil.copy("/opt/program/tmp/tika-server.jar", "../../tmp/tika-server.jar")
        else:
            shutil.copy("/opt/program/tmp/tika-server.jar", "../../tmp/tika-server.jar")
        
        if path.exists("../../tmp/tika.log"):
            os.remove("../../tmp/tika.log")
            shutil.copy("/opt/program/tmp/tika.log", "../../tmp/tika.log")
        else:
            shutil.copy("/opt/program/tmp/tika.log", "../../tmp/tika.log")
        
    except Exception as e:
        return flask.Response(response="Error in copying ",status=515,mimetype='text/plain')
    
    try:
        
        if not os.path.exists(filepath):
            return flask.Response(response="Give name of the zip file as Input.zip which contain a file named Input: where the .pdf is present ",status=505,mimetype='text/plain')
        
        #print(filepath)
        #filepath = "../input/2014 - Annual Report - Panalpina Welttransport Holding AG.pdf"
        
        Dict = get_pages(filepath)
        json_obj = json.dumps(Dict)
        try:
            os.remove("../../tmp/tika-server.log")
            os.remove("../../tmp/tika-server.jar.md5")
            os.remove("../../tmp/tika-server.jar")
            os.remove("../../tmp/tika.log")
        except Exception as e:
            return flask.Response(response="Error in removing ",status=515,mimetype='text/plain')
        return flask.Response(response=json_obj, status=200, mimetype='application/json')
    except Exception as e:
        return flask.Response(response="Error Log"+str(e),status=415,mimetype='text/plain')


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080,debug=True)
