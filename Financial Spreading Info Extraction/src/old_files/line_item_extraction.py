
import os
import pandas as pd

import numpy as np
import re
from fuzzywuzzy import fuzz 

from both_assets_liab_present import both_assets_liabilities
from only_liabilities_table import only_liabilities_table
from only_Assets_table import only_Assets_table
from balance_sheet_direct_line_items import balance_sheet_direct_line_items
from profit_and_loss_direct_line_items import profit_and_loss_direct_line_items
from cash_flow_direct_line_items import cash_flow_direct_line_items

def line_items(table_name,table_dir,pdf,table_type):
    # table_name = table_names[j]
    # pdf = pdf_list[j]
    #### Read the table from textract
    table_data = pd.read_csv(os.path.join(table_dir,table_name +".tsv"),header=None,sep="\t")
    
    #table_data.to_csv("temp_"+ pdf+".csv", index = True)
    ##############################
    #get the relevent year values
    ##############################
    key_words_heading = ["march", "march 31", "31 march", "31", "note",
                         "notes", "particulars","2014","2015","2016","2013","dec","mar","december",
                         "million","13","14","15","16","17","$"]
    
    percentage_head = []
    for z in range(table_data.shape[0]):
        table_data.iloc[z,:] = table_data.iloc[z,:].str.lower()
        row_content = ""
        for l in range(len(table_data.iloc[z,:])):
            row_content = row_content + str(table_data.iloc[z,:][l])
        number_of_matching_head = 0
        for i in key_words_heading:
            if i in row_content:
                number_of_matching_head = number_of_matching_head + 1
        percentage_head.append(number_of_matching_head*100/len(key_words_heading))
        
    rel_row = percentage_head.index(max(percentage_head))
    cell_num_sum = []
    
    for f in table_data.iloc[rel_row,:]:
        heading_string = str(f)
        temp = re.findall(r'\d+', heading_string) 
        res = list(map(int, temp))
        cell_num_sum.append(sum(res))
    year_col = cell_num_sum.index(max(cell_num_sum))
    ##############################
    #get the column where values names are present
    ##############################
    if table_type == "balance sheet":
        key_words = ["assets","liabilities","total assets","total liabilities", "cash", "inventory", "revenue", "depts",
                 "receivable","intangible","payable","equity","share capital"]
    elif table_type == "cash flow":
        key_words = ["assets","liabilities","total assets","total liabilities", "cash", "inventory", "revenue", "depts",
                 "receivable","intangible","payable","equity","share capital"]
    elif table_type == "Profit and Loss":
        key_words = ["profit","revenue", "operating", "income tax", "expenses"]
       
    table_data = table_data.fillna("NULL")
    percentage = []
    for k in range(table_data.shape[1]):
        table_data.iloc[:,k] = table_data.iloc[:,k].str.lower()
        column_content = ""
        for l in range(len(table_data.iloc[:,k])):
            column_content = column_content + str(table_data.iloc[:,k][l])
        number_of_matching = 0
        for i in key_words:
            if i in column_content:
                number_of_matching = number_of_matching + 1
        percentage.append(number_of_matching*100/len(key_words))
        
    rel_col = percentage.index(max(percentage))
    
    ##############################
    #extract common line items
    ##############################
    list_col = list(table_data.iloc[:,rel_col].str.lower())
    
    
    ##############################################################################################################
    ##############################################################################################################
    if table_type == "cash flow":
        lst, given_lst = cash_flow_direct_line_items(list_col,table_data,year_col,rel_col)
    
    ##############################################################################################################
    ##############################################################################################################
    elif table_type == "Profit and Loss":
        lst, given_lst = profit_and_loss_direct_line_items(list_col,table_data,year_col,rel_col)
        return lst, given_lst
    ##############################################################################################################
    ##############################################################################################################
    ##############################
    elif table_type == "balance sheet":
        lst, given_lst = balance_sheet_direct_line_items(list_col,table_data,year_col,rel_col)
    
        #extact line items in the form of "others" formats
        ##############################
        check_list = []
        check_list_names = ["Assets_table","liabilities_table","non_current_assets_table","current_assets_table",
                            "non_current_liabilities_table","current_liabilities_table"]
        
        
        Assets_position = list(np.where((table_data.iloc[:,rel_col].str.contains('assets')).fillna(False).astype(bool))[0])
        liabilities_position = list(np.where((table_data.iloc[:,rel_col].str.contains('liabilities')).fillna(False).astype(bool))[0])
        
        mid_tables_dir = "./data_results"
        data_results_dir = "./mid_tables"
        if not os.path.exists(mid_tables_dir):
            os.makedirs(mid_tables_dir)
        if not os.path.exists(data_results_dir):
            os.makedirs(data_results_dir)
    ##################################################################################################################################    
        if len(Assets_position) == 0:
            #print("1")
            only_liabilities_table(table_data,liabilities_position,table_name,check_list,check_list_names,list_col,lst,given_lst,year_col,rel_col)
    ##################################################################################################################################
        if len(liabilities_position) == 0:
            #print("2")
            only_Assets_table(table_data,Assets_position,table_name,check_list,check_list_names,list_col,lst,given_lst,year_col,rel_col)
    ##################################################################################################################################   
        if (len(Assets_position) != 0 and len(liabilities_position) != 0):
            #print("3")
            both_assets_liabilities(Assets_position,liabilities_position,table_data,table_name,check_list,check_list_names,list_col,lst,given_lst,year_col,rel_col)
    ##################################################################################################################################  
        if (len(Assets_position) == 0 and len(liabilities_position) == 0):
            #print("4")
            result = pd.DataFrame()
        ############################################################################################################################
        ############################################################################################################################