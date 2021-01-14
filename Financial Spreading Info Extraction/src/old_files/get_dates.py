# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 11:16:39 2021

@author: thrinath.nelaturi
"""
import spacy
import dateparser
import regex as re

nlp = spacy.load('en_core_web_sm')
#text = content[page - 1]

def get_dates(text):
    doc = nlp(text)
    dates_present = []
    for entity in doc.ents:
        if entity.label_ == "DATE":
            #print(entity.text)
            dates_present.append(entity.text)
    years = []
    for k in dates_present:
        years.append(re.findall(r"\b(2\d{3})\b",k))
    combined = []
    for l in years:
        combined = combined + l
    all_years = list(set(combined))
    
    
    return all_years