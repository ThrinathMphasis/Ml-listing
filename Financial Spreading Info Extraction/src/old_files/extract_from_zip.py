import os
from zipfile import ZipFile
import shutil
import pandas as pd
import json 

def extract(zip):
    '''
    Gets a zip file as input which contain, parameters from .json file and data from .csv file

    Parameters
    ----------
    zip : .zip file
        extracts to Input file 

    Returns
    -------
    file_path = path of pdf file

    '''
    extracted_folder = os.path.join(os.getcwd(),'../Input')
    
    if not os.path.exists(extracted_folder):
        os.makedirs(extracted_folder)
    else:
        shutil.rmtree(extracted_folder)
        os.makedirs(extracted_folder)
    try:
        with ZipFile(zip, 'r') as zipObj:
            zipObj.extractall(path=extracted_folder)
            #print('######### zip extracted into Input folder #########')
    except Exception as e:
        print(e)
    
    try:
        
        print("1")
        open_file = os.path.join(os.getcwd(),'../Input/Input')
        if not os.path.exists(open_file):
            open_file = os.path.join(os.getcwd(),'../Input')
        for r, d, f in os.walk(open_file):
            for file in f:
                if '.pdf' in file:
                    #print("HI")
                    filepath=os.path.join("../Input/Input",file)
                    if not os.path.exists(open_file):
                        filepath=os.path.join("../Input",file)
                    #print(filepath)
                    
        return filepath
    except Exception as e:
        print(e)
        return e