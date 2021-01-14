# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os   
from tika import parser
import fitz
import re
import pandas as pd
#from find_table_pages import get_pages_with_tables as get_table_pages

#filepath = file_path
def extract_content(filepath):
    raw_xml = parser.from_file(filepath, xmlContent=True)
    body = raw_xml['content'].split('<body>')[1].split('</body>')[0]
    body_without_tag = body.replace("<p>", "").replace("</p>", "").replace("<div>", "").replace("</div>","").replace("<p />","").replace("<b>", "").replace("</b>", "")
    text_pages = body_without_tag.split("""<div class="page">""")[1:]
    table_content = []
    for each_page in text_pages:
        table_content.append(table_data(each_page))
        
    return text_pages, table_content



def table_data(page_content):
    #page_content = text_pages[0]
    ''' Parameters
    ----------
    page_content : List containing extracted content of each page
    DESCRIPTION. Returns
    -------
    None. '''
    list_sents = page_content.split("\n\n")
    table_rows = []
    para = []
    for each in list_sents:
        if "." in each[-5:]:
            if each[-5:].split('.')[1].isalnum():
                table_rows.append(each)
            else:
                para.append(each)
        else:
            table_rows.append(each)
    #print("paragraphs",para)
    #print("table_row",table_rows)
    return table_rows


def extract_headings(filepath):
    data= []
    page_headings={}
    doc = fitz.open(filepath)
    for page in doc:
        html_text = page.getText("xhtml")
        data.append(html_text)
    for index, value in enumerate(data):
        page_headings[str(index+1)]=re.findall("<h\d>(.*?)</h\d>", value)
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
    content, content_table = extract_content(file_path)
    headings = extract_headings(file_path)
    table_pages = word_count_table_pages(content)
    #table_pages = get_table_pages(file_path)
    return content, content_table, headings, table_pages



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


#file_path =  "C:/Users/thrinath.nelaturi/Desktop/Paypal/Table selection/Non-airline document/2014 - Annual Report - Schindler Holding Ltd.pdf"
def get_pages(content, content_table, headings, table_pages, headings_keywords, headings_keywords_not,
              level_1_keywords, level_2_keywords):
    
    # headings_keywords = headings_keywords_balance_sheet
    # headings_keywords_not = heading_keywords_not_balance_sheet
    # level_1_keywords = level_1_keywords_balance_sheet
    # level_2_keywords = level_2_keywords_balance_sheet
    relevent_page_content = {}
    relevent_page_headings = {}
    for i in table_pages:
        relevent_page_content[i]=content[i-1]
    
    for j in table_pages:
        relevent_page_headings[j]=headings[str(j)]
    
    level_1_keywords = [x.lower() for x in level_1_keywords]
    level_2_keywords = [x.lower() for x in level_2_keywords]
    headings_keywords = [x.lower() for x in headings_keywords]
    headings_keywords_not = [x.lower() for x in headings_keywords_not]
    
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
    #pdf_name = "2014 - Annual Report - Schindler Holding Ltd"
    
    file_path = filepath
    
    #file_path = "C:/Users/thrinath.nelaturi/Desktop/Paypal/Table selection/Non-airline document/Input/2014-2015 - Annual Report - Bharti Airtel Limited.pdf"
    
    #################################################################################################################
    
    headings_keywords_cash_flow = ["Consolidated statement of cash flows", "Cash Flow Statement",
                                   "Consolidated cash flow statement","cash flow","cash"]
    headings_keywords_not_cash_flow = ["notes","Consolidated Statement of Profit and Loss","Statement of Profit and Loss",
                          "Standalone Statement of Profit and Loss", "Profit and Loss", "Profit & Loss","Profit or Loss",
                          "Profit/Loss", "Consolidated Income statement", "Income","consolidated balance sheet","consolidated statement of financial position",
                          "balance sheet", "financial position", "consolidated Balance sheet","standalone balance sheet",
                          "key figures"]
    
    level_1_keywords_cash_flow = ["operating","operational","operation","operations","Income tax","Net cash","plant","equipment","Property", 
                                  "equipment","cash equivalents","cash flow","Net", "profit","interests","Exchange","balance"]
    
    level_2_keywords_cash_flow = ["interest recived", "dividends","Goodwill","Share","Income taxes paid","Dividends",
                                  "Employee","Depreciation","amortization","impairment","Opening balance","closing balance"]
    #################################################################################################################
    
    headings_keywords_profit_loss = ["Consolidated Statement of Profit and Loss","Statement of Profit and Loss",
                          "Standalone Statement of Profit and Loss", "Profit and Loss", "Profit & Loss","Profit or Loss",
                          "Profit/Loss", "Consolidated", "Consolidated Income statement", "Income","Income statement",
                          "CONSOLIDATED STATEMENT OF COMPREHENSIVE INCOME"]
    headings_keywords_not_profit_loss = ["notes","consolidated balance sheet","consolidated statement of financial position",
                          "balance sheet", "financial position", "consolidated Balance sheet","key figures","facts and figures",
                          "standalone balance sheet","Consolidated statement of cash flows", "Cash Flow Statement",
                          "Consolidated cash flow statement","Consolidated statements of cash flows","Income tax expences"]
    
    level_1_keywords_profit_loss = ["Income/ Revenue", "Income", "Revenue", "Income/Revenue",
                                      "Revenue from Operations", "Total Income","Expense",  
                                      "Total Expenses" ,"Total Expenditure", "Expenses", "Expenditure",
                                      "Profit before Tax", "profit", "Tax", "Tax Expense", "Current Tax"
                                      "Deferred Tax", "Total Tax Expense", 
                                      "profit for the year/ profit after tax", "profit for the year", "profit after tax",
                                      "key figures","key figure"]
    
    level_2_keywords_profit_loss = ["other income", "cost of materials consumed", "Employees benfit Expense",
                                     "cost of materials", "Employees benfit", "Employee benfits", "Employees Expense",
                                     "Employee Expenses","cost of goods"]
    
    ###########################################
    
    headings_keywords_balance_sheet = ["consolidated balance sheet","consolidated statement of financial position",
                          "balance sheet", "financial position", "consolidated Balance sheet",
                          "standalone balance sheet", "consolidated"]
    heading_keywords_not_balance_sheet = ["notes", "cash flow","Consolidated Statement of Profit and Loss","Statement of Profit and Loss",
                          "Standalone Statement of Profit and Loss", "Profit and Loss", "Profit & Loss","Profit or Loss",
                          "Profit/Loss", "Consolidated Income statement", "Income","CONSOLIDATED STATEMENT OF CASH FLOWS", "Cash Flow Statement",
                          "Consolidated cash flow statement","key figures"]
    
    level_1_keywords_balance_sheet = ["balance sheet","financial position","Assets", "Non Current Assets", "CURRENT ASSETS", "Inventories",
                                      "Financial Assets", "Total Assets", "EQUITY AND LIABILITIES" ,
                                      "EQUITY", "Share capital, Equity Share Capital", "Total Equity", "LIABILITIES"
                                      "Non-current liabilities", "Current liabilities", "Borrowings", 
                                      "Trade and other payables, Trade Payables", "Provisions",
                                      "Total Liabilities","key figures","key figure", "financial position"]
    
    level_2_keywords_balance_sheet = ["Property Plan and Equipment", "Intangible Assets", "Capital Work-in-Progress",
                                      "Goodwill", "Trade receivables", 
                                      "Long Term Loans and Advances, Loans receivable, Loans",
                                      "Financial Assets", "Trade Receivables, Trade and other receivables",
                                      "Cash and Bank Balances, Cash and cash equivalents",
                                      "Other Current Assets", "Interest-bearing borrowings, Borrowings",
                                      "Property Plan", "Equipment", "Long Term Loans", "Loans receivable", "Loans",
                                      "Trade Receivables", "Trade", "other receivables", 
                                      "Cash balances", "Bank Balances", "Cash", "cash equivalents",
                                      "Borrowings"]
    
    #################################################################################################################
    
    content, content_table, headings, table_pages = pre_req(file_path)
    
    ###########################
    df_results_cash_flow, raw_table = get_pages(content, content_table, headings, table_pages, headings_keywords_cash_flow, headings_keywords_not_cash_flow,
              level_1_keywords_cash_flow, level_2_keywords_cash_flow)    
    
    relevent_page_numbers_cash_flow = list(df_results_cash_flow.Page_number)
    ###########################
    df_results_profit_loss, raw_table = get_pages(content, content_table, headings, table_pages, headings_keywords_profit_loss, headings_keywords_not_profit_loss,
              level_1_keywords_profit_loss, level_2_keywords_profit_loss)    
    
    relevent_page_numbers_profit_loss = list(df_results_profit_loss.Page_number)
    ###########################
    
    df_results_balance_sheet , raw_table= get_pages(content, content_table, headings, table_pages, headings_keywords_balance_sheet, heading_keywords_not_balance_sheet,
              level_1_keywords_balance_sheet, level_2_keywords_balance_sheet)    
    
    relevent_page_numbers_balance_sheet = list(df_results_balance_sheet.Page_number)
    return content,relevent_page_numbers_balance_sheet, relevent_page_numbers_cash_flow, relevent_page_numbers_profit_loss