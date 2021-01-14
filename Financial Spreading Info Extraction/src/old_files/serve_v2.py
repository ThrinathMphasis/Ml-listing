#!/usr/bin/env python3

from flask import Flask, request, Response
from pages import get_pages
from extract_from_zip import extract
import os
import json
import time

class modelError(Exception):
    pass

app = Flask(__name__)

@app.route('/ping',methods = ['GET'])
def ping():
  """Determine if the container is working and healthy. In this sample container, we declare
  it healthy if we can load the model successfully."""
  status = 200

  return Response(response='ping success', status=status, mimetype='application/json')


@app.route('/invocations',methods=['POST'])
def testing():
    start_time = time.time()
    if request.content_type == 'application/zip':
        try:
            data_file = request.data
            with open('Input.zip','wb') as f:
                f.write(data_file)
        
            # Input has config as well as input data. following function extracts both
            filepath = extract('Input.zip')
            print(filepath)
        except Exception as e:
            return Response(response="Input file is not utf-8 encoded please upload utf-8 encoded file - Error log:"+str(e),status=500,mimetype='text/plain')

        try:
            middle_time = time.time()
            print("rime till point 1:")
            print(middle_time - start_time)
            if not os.path.exists(filepath):
                return Response(response="Give name of the zip file as Input.zip which contain a file named Input: where the .pdf is present ",status=500,mimetype='text/plain')
            print("created file Input")
            model_start_time = time.time()
            Dict = get_pages(filepath)
            print(Dict)
            model_end_time = time.time()
            print("model time:")
            print(model_end_time - model_start_time)
            json_obj = json.dumps(Dict)
            print("json created")
            return Response(response=json_obj,status=200,mimetype='application/json')
        except Exception as e:
            return Response(response="Error Log"+str(e),status=500,mimetype='text/plain')
    else:
        return Response(response="This algorithm works only on .pdf file present in .zip file, please refer Documentation's Usage instructions for the same",status=500,mimetype='text/plain')

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8080)
