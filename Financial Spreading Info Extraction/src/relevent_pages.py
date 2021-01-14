# -*- coding: utf-8 -*-

import os   
from tika import parser
import fitz
import re
import pandas as pd

def extract_content(filepath):
    print("--I--")
    raw_xml = parser.from_file(filepath, xmlContent=True)
    print("--II--")
    body = raw_xml['content'].split('<body>')[1].split('</body>')[0]
    print("--III--")
    body_without_tag = body.replace("<p>", "").replace("</p>", "").replace("<div>", "").replace("</div>","").replace("<p />","").replace("<b>", "").replace("</b>", "")
    text_pages = body_without_tag.split("""<div class="page">""")[1:]
    return text_pages




def extract_headings(filepath):
    data= []
    page_headings={}
    print("--i--")
    doc = fitz.open(filepath)
    print("--ii--")
    for page in doc:
        html_text = page.getText("xhtml")
        data.append(html_text)
    for index, value in enumerate(data):
        page_headings[str(index+1)]=re.findall("<h\d>(.*?)</h\d>", value)
    print("--iii--")
    return page_headings

def word_count_table_pages(content):
    num_words = []
    page_numbers = []
    table_pages = []
    for i in range(len(content)):
        page_numbers.append(i+1)
        num_words.append(len(content[i].split()))
        if len(content[i].split()) < 400:
            table_pages.append(i+1)
    return table_pages

def pre_req(file_path):
    print("3")
    content = extract_content(file_path)
    print("4")
    headings = extract_headings(file_path)
    print("5")
    table_pages = word_count_table_pages(content)
    print("6")
    return content, headings, table_pages



def heading_extractor(filepath):
    data= []
    page_headings={}
    doc = fitz.open(filepath)
    for page in doc:
        html_text = page.getText("xhtml")
        data.append(html_text)
    for index, value in enumerate(data):
        headings = re.findall("<H\d>(.*?)</H\d>", value.upper())
        bold_subsection = re.findall("<B>(.*?)</B>", value.upper())
        bold_subsection_f = [ _x for _x in bold_subsection if len(_x)>10 ]
    
    page_headings["PageNo-"+str(index)]={"headings":headings, "bold_section":bold_subsection_f}
    print("Heading extraction complete")
    return page_headings,data



def get_pages(content, headings, table_pages, headings_keywords, headings_keywords_not,
              level_1_keywords, level_2_keywords):
    
    relevent_page_content = {}
    relevent_page_headings = {}
    for i in table_pages:
        relevent_page_content[i]=content[i-1]
        relevent_page_headings[i]=headings[str(i)]
    
    
    page_number = [] 
    level_1_percentage_col = []
    level_2_percentage_col = []
    all_headlines = []
    for k, v in relevent_page_content.items():
        words_matching_level_1 = []
        num_words_matching_level_1 = 0
        for b in level_1_keywords:
            if b in v.lower():
               words_matching_level_1.append(b)
               num_words_matching_level_1 = num_words_matching_level_1 + 1
        words_matching_level_2 = []
        num_words_matching_level_2 = 0  
        for c in level_2_keywords:
            if c in v.lower():
               words_matching_level_2.append(b)
               num_words_matching_level_2 = num_words_matching_level_2 + 1
        
        level_1_percentage = num_words_matching_level_1*100/len(level_1_keywords)
        #print(level_1_percentage)
        level_2_percentage = num_words_matching_level_2*100/len(level_2_keywords)
        #print(level_2_percentage)
        
        page_number.append(k)
        level_1_percentage_col.append(level_1_percentage)
        level_2_percentage_col.append(level_2_percentage)
        all_headlines.append(headings[str(k)])
    df = pd.DataFrame(list(zip(page_number, level_1_percentage_col, level_2_percentage_col, all_headlines)), 
               columns =['Page_number', 'Level_1', 'Level_2', 'Headings'])
    df.reset_index()
    df = df.sort_values(by='Level_1', ascending=False)
    #print(df)
    relevent_pages = df[:15]
    relevent_pages = relevent_pages[relevent_pages.astype(str)['Headings'] != '[]']
    df3 = relevent_pages.copy(deep=True)
    
    for k in list(relevent_pages["Headings"]):
        for l in headings_keywords_not:
            for m in k:
                if l in m.lower():
                    relevent_pages = relevent_pages[relevent_pages.astype(str)['Headings'] != str(k)]
    
    relevent_headings = []
    for w in list(relevent_pages["Headings"]):
        for b in headings_keywords:
            for n in w:
                if str(b) in str(n).lower():
                    if str(w) not in relevent_headings:
                        relevent_headings.append(str(w))
    #print(relevent_headings)            
    relevent_pages = relevent_pages.loc[relevent_pages.astype(str)['Headings'].isin(relevent_headings)]
    
    return relevent_pages, df3

def extract(filepath):
    
    file_path = filepath
    
    
    #################################################################################################################
    
    headings_keywords_cash_flow = ["consolidated statement of cash flows", "cash flow statement",
                                   "consolidated cash flow statement","cash flow","cash"]
    headings_keywords_not_cash_flow = ["notes","consolidated statement of profit and loss","statement of profit and loss",
                          "standalone statement of profit and loss", "profit and loss", "profit & loss","profit or loss",
                          "profit/loss", "consolidated income statement", "income","consolidated balance sheet","consolidated statement of financial position",
                          "balance sheet", "financial position", "consolidated Balance sheet","standalone balance sheet",
                          "key figures"]
    
    level_1_keywords_cash_flow = ["operating","operational","operation","operations","income tax","net cash","plant","equipment","property", 
                                  "equipment","cash equivalents","cash flow","net", "profit","interests","exchange","balance"]
    
    level_2_keywords_cash_flow = ["interest recived", "dividends","goodwill","share","income taxes paid","dividends",
                                  "employee","depreciation","amortization","impairment","opening balance","closing balance"]
    #################################################################################################################
    
    headings_keywords_profit_loss = ["consolidated statement of profit and loss","statement of profit and loss",
                          "standalone statement of profit and loss", "profit and loss", "profit & loss","profit or loss",
                          "profit/loss", "consolidated", "consolidated income statement", "income","income statement",
                          "consolidated statement of comprehensive income"]
    headings_keywords_not_profit_loss = ["notes","consolidated balance sheet","consolidated statement of financial position",
                          "balance sheet", "financial position", "consolidated balance sheet","key figures","facts and figures",
                          "standalone balance sheet","consolidated statement of cash flows", "cash flow statement",
                          "consolidated cash flow statement","consolidated statements of cash flows","income tax expences"]
    
    level_1_keywords_profit_loss = ["income/ revenue", "income", "revenue", "income/revenue",
                                      "revenue from operations", "total income","expense",  
                                      "total expenses" ,"total expenditure", "expenses", "expenditure",
                                      "profit before tax", "profit", "tax", "tax expense", "current tax"
                                      "deferred tax", "total tax expense", 
                                      "profit for the year/ profit after tax", "profit for the year", "profit after tax",
                                      "key figures","key figure"]
    
    level_2_keywords_profit_loss = ["other income", "cost of materials consumed", "employees benfit expense",
                                     "cost of materials", "employees benfit", "employee benfits", "employees expense",
                                     "employee expenses","cost of goods"]
    
    ###########################################
    
    headings_keywords_balance_sheet = ["consolidated balance sheet","consolidated statement of financial position",
                          "balance sheet", "financial position", "consolidated Balance sheet",
                          "standalone balance sheet", "consolidated"]
    heading_keywords_not_balance_sheet = ["notes", "cash flow","consolidated statement of profit and loss","statement of profit and loss",
                          "standalone statement of profit and loss", "profit and loss", "profit & loss","profit or loss",
                          "profit/loss", "consolidated income statement", "income","consolidated statement of cash flow", "cash flow statement",
                          "consolidated cash flow statement","key figures"]
    
    level_1_keywords_balance_sheet = ["balance sheet","financial position","assets", "non current assets", "current assets", "inventories",
                                      "financial assets", "total assets", "equity and liabilities" ,
                                      "equity", "share capital, equity share capital", "total equity", "liabilities"
                                      "non-current liabilities", "current liabilities", "borrowings", 
                                      "trade and other payables, trade payables", "provisions",
                                      "total liabilities","key figures","key figure", "financial position"]
    
    level_2_keywords_balance_sheet = ["property plan and equipment", "intangible assets", "capital work-in-progress",
                                      "goodwill", "trade receivables", 
                                      "long term loans and advances", "loans receivable", "loans",
                                      "financial assets", "trade receivables, trade and other receivables",
                                      "cash and bank balances", "cash and cash equivalents",
                                      "other current assets", "interest-bearing borrowings", "borrowings",
                                      "property plan", "equipment", "long term loans", "loans receivable", "loans",
                                      "trade receivables", "trade", "other receivables", 
                                      "cash balances", "bank balances", "cash", "cash equivalents",
                                      "borrowings"]
    
    #################################################################################################################
    print("start function")
    content, headings, table_pages = pre_req(file_path)
    print("end function")
    ###########################
    df_results_cash_flow, raw_table = get_pages(content, headings, table_pages, headings_keywords_cash_flow, headings_keywords_not_cash_flow,
              level_1_keywords_cash_flow, level_2_keywords_cash_flow)    
    
    relevent_page_numbers_cash_flow = list(df_results_cash_flow.Page_number)
    ###########################
    df_results_profit_loss, raw_table = get_pages(content, headings, table_pages, headings_keywords_profit_loss, headings_keywords_not_profit_loss,
              level_1_keywords_profit_loss, level_2_keywords_profit_loss)    
    
    relevent_page_numbers_profit_loss = list(df_results_profit_loss.Page_number)
    ###########################
    
    df_results_balance_sheet , raw_table= get_pages(content, headings, table_pages, headings_keywords_balance_sheet, heading_keywords_not_balance_sheet,
              level_1_keywords_balance_sheet, level_2_keywords_balance_sheet)    
    
    relevent_page_numbers_balance_sheet = list(df_results_balance_sheet.Page_number)
    return content,relevent_page_numbers_balance_sheet, relevent_page_numbers_cash_flow, relevent_page_numbers_profit_loss
