# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 16:18:15 2021

@author: thrinath.nelaturi
"""
from fuzzywuzzy import fuzz 

def get_cash_flow_direct_line_items(page_content):
    page_content = page_content.lower()
    paragraphs = page_content.split("\n\n")
    all_lines = []
    for para in paragraphs:
        lines = para.split("\n")
        for k in lines:
            all_lines.append(k)
    
    list_col = all_lines
    
    
    def net_income(list_col):
           
        for row in list_col:
            if fuzz.WRatio("Net Income", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("Consolidated profit", row)>90:
                return list_col.index(row)
            elif "net income" in str(row):
                return list_col.index(row)
            elif "consolidated profit" in str(row):
                return list_col.index(row)
    
    def cash_flow_from_operating_activities(list_col):
        for row in list_col:
            if fuzz.WRatio("Cash Flow from Operating Activities", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("Operating Activities", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("Net cash from operating activities", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("Net cash inflow from operating activities", row)>90:
                return list_col.index(row)
            elif "operating activities" in str(row):
                return list_col.index(row)
    
    def cash_flow_from_financing_activities(list_col):
        for row in list_col:
            if fuzz.WRatio("Cash Flow from Financing Activities", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("Financing Activities", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("Net cash from financing activities", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("Net cash flows used in financing activities", row)>90:
                return list_col.index(row)
            elif "financing activities" in str(row):
                return list_col.index(row)
    
    def cash_flow__from_investing_activities(list_col):
        for row in list_col:
            if fuzz.WRatio("Cash Flow from Investing Activities", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("Investing Activities", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("Net cash from Investing activities", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("Net cash flows used in Investing activities", row)>90:
                return list_col.index(row)
            elif "investing activities" in str(row):
                return list_col.index(row)
    
    def depreciation(list_col):
        for row in list_col:
            if fuzz.WRatio("Depreciation", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("devaluation", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("Depreciation of property, plant& equipment", row)>90:
                return list_col.index(row)
            elif "depreciation" in str(row):
                if "amortization" not in str(row):
                    return list_col.index(row)
    
    def amortization(list_col):
        for row in list_col:
            if fuzz.WRatio("amortization", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("amortised cost", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("amortization of intangible assets", row)>90:
                return list_col.index(row)
            elif "amortization" in str(row):
                if "depreciation" not in str(row):
                    return list_col.index(row)
    
    def sum_of_amor_depr_impair(list_col):
        for row in list_col:
            if fuzz.WRatio("depreciation, amortization and impairment", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("depreciation and amortization expense", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("depreciation and amortization", row)>90:
                return list_col.index(row)
            elif "amortization" in str(row):
                if "depreciation" in str(row):
                    return list_col.index(row)
    
    
    def account_receivables(list_col):
        for row in list_col:
            if fuzz.WRatio("account receivables", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("trade receivables", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("receivables", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("trade and other receivables", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("notes receivables", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("intrest receivables", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("other receivables", row)>90:
                return list_col.index(row)
            elif "receivables" in str(row):
                return list_col.index(row)
    
    def inventory(list_col):
            
        for row in list_col:
            if fuzz.WRatio("inventory", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("inventories", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("raw materials", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("work in progress", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("finished product", row)>90:
                return list_col.index(row)
            elif "inventories" in str(row):
                return list_col.index(row)
            elif "inventory" in str(row):
                return list_col.index(row)
    
    def account_payable(list_col):
        
        for row in list_col:
            if fuzz.WRatio("account payables", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("trade payables", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("trade and other payables", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("payables", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("income taxes payables", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("intrest payables", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("accrued payables", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("unearned payables", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("salaries payables", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("rent payables", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("utilities payables", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("mortgage payables", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("other payables", row)>90:
                return list_col.index(row)
            elif "payables" in str(row):
                return list_col.index(row)
    
    def deferred_revenue(list_col):
        
        for row in list_col:
            type(row)
            if fuzz.WRatio("deferred revenue", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("unearned revenue", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("deferred liabilities", row)>90:
                return list_col.index(row)
            elif "deferred revenue" in str(row):
                return list_col.index(row)
            elif "deferred liabilities" in str(row):
                return list_col.index(row)
            elif "unearned revenue" in str(row):
                return list_col.index(row)
            
    def intangible_assets(list_col):
            
        for row in list_col:
            if fuzz.WRatio("intangible assets", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("intangible", row)>90:
                return list_col.index(row)
            if "intangible assets" in str(row):
                return list_col.index(row)
            elif "intangible" in str(row):
                return list_col.index(row)
            
    
    depreciation_row = depreciation(list_col)
    amortization_row = amortization(list_col)
    sum_of_amor_depr_impair_row = sum_of_amor_depr_impair(list_col)
    
    net_income_row = net_income(list_col)
    cash_flow_from_operating_activities_row = cash_flow_from_operating_activities(list_col)
    cash_flow_from_financing_activities_row = cash_flow_from_financing_activities(list_col)
    cash_flow__from_investing_activities_row = cash_flow__from_investing_activities(list_col)
    account_receivables_row = account_receivables(list_col)
    inventory_row = inventory(list_col)
    account_payable_row = account_payable(list_col)
    deferred_revenue_row = deferred_revenue(list_col)
    intangible_assets_row = intangible_assets(list_col)
    
    # total_assets_row = total_assets(list_col)
    # account_payable_row = account_payable(list_col)
    # deferred_revenue_row = deferred_revenue(list_col)
    # total_liabilities_row = total_liabilities(list_col)
    # total_equity_row = total_equity(list_col)
    # retained_earnings_row = retained_earnings(list_col)
    # share_capital_row = share_capital(list_col)
    # special_reserve_row = special_reserve(list_col)
    # total_equity_and_liablities_row = total_equity_and_liablities(list_col)
    
    line_items = {}
    
    if (depreciation_row != None) and (amortization_row != None):
        line_items["Non-cash expenses (depreciation+amortization)"] = list_col[depreciation_row]+list_col[amortization_row]
        
    elif sum_of_amor_depr_impair_row != None:
        line_items["Non-cash expenses (depreciation+amortization)"] = list_col[sum_of_amor_depr_impair_row]
    else:
        line_items["Non-cash expenses (depreciation+amortization)"] = "Not Found"
        
    if net_income_row != None:
        line_items["net_income"] = list_col[net_income_row]
        
    else:
        line_items["net_income"] = "Not Found"
        
    if cash_flow_from_operating_activities_row != None:
        line_items["cash_flow_from_operating_activities"] = list_col[cash_flow_from_operating_activities_row]
        
    else:
        line_items["cash_flow_from_operating_activities"] = "Not Found"
        
    if cash_flow_from_financing_activities_row != None:
        line_items["cash_flow_from_financing_activities"] = list_col[cash_flow_from_financing_activities_row]
        
    else:
        line_items["cash_flow_from_financing_activities"] = "Not Found"
        
    if cash_flow__from_investing_activities_row != None:
        line_items["cash_flow__from_investing_activities"] = list_col[cash_flow__from_investing_activities_row]
        
    else:
        line_items["cash_flow__from_investing_activities"] = "Not Found"
        
    if account_receivables_row != None:
        line_items["account_receivables"] = list_col[account_receivables_row]
        
    else:
        line_items["account_receivables"] = "Not Found"
    
    if inventory_row != None:
        line_items["inventory"] = list_col[inventory_row]
        
    else:
        line_items["inventory"] = "Not Found"
        
    if account_payable_row != None:
        line_items["account_payable"] = list_col[account_payable_row]
        
    else:
        line_items["account_payable"] = "Not Found"
    
    if deferred_revenue_row != None:
        line_items["deferred_revenue"] = list_col[deferred_revenue_row]
        
    else:
        line_items["deferred_revenue"] = "Not Found"
    
    if intangible_assets_row != None:
        line_items["intangible_assets"] = list_col[intangible_assets_row]
        
    else:
        line_items["intangible_assets"] = "Not Found"
    
    return line_items

