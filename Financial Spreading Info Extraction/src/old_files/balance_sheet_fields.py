# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 14:47:14 2021

@author: thrinath.nelaturi
"""
from fuzzywuzzy import fuzz 


#page_content = Dict['balance_sheet']["page.No:191"]["Content"]
def get_balance_sheet_line_items(page_content):
    page_content = page_content.lower()
    paragraphs = page_content.split("\n\n")
    all_lines = []
    for para in paragraphs:
        lines = para.split("\n")
        for k in lines:
            all_lines.append(k)
    
    list_col = all_lines
    
    def cash_and_cash_equivalent(all_lines):
           
        for row in list_col:
            if fuzz.WRatio("cash and cash equivalents", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("cash equivalents", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("cash", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("foreign currency", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("currency", row)>90:
                return list_col.index(row)
            elif "cash" in str(row):
                return list_col.index(row)
            elif "cash equivalents" in str(row):
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
    
    def property_plant_and_equipment(list_col):
            
        for row in list_col:
            if fuzz.WRatio("property, plant and equipment", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("plant and equipment", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("non-current investments", row)>90:
                return list_col.index(row)
            elif "pp&e" in str(row):
                return list_col.index(row)
            elif "ppe" in str(row):
                return list_col.index(row)
            elif "plant" in str(row):
                return list_col.index(row)
            elif "equipment" in str(row):
                return list_col.index(row)
            elif "property" in str(row):
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
    
    def total_assets(list_col):
            
        for row in list_col:
            if fuzz.WRatio("total assets", row)>90:
                return list_col.index(row)
            elif "total assets" in str(row):
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
            
    
    def total_liabilities(list_col):
        for row in list_col:
            if fuzz.WRatio("total liabilities", row)>95:
                return list_col.index(row)
            elif "total liabilities" in str(row):
                return list_col.index(row)
    
    def total_equity(list_col):
            
        for row in list_col:
            if fuzz.WRatio("total equity", row)>95:
                return list_col.index(row)
            elif "total equity" in str(row):
                return list_col.index(row)
                 
    def retained_earnings(list_col):
        
        for row in list_col:
            if fuzz.WRatio("retained earnings", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("deferred liabilities", row)>95:
                return list_col.index(row)
            elif fuzz.WRatio("retained profits", row)>95:
                return list_col.index(row)
            elif fuzz.WRatio("retained surplus", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("undistributed profits", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("accumulated profits", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("undivided profits", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("earned surplus", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("reserves and surplus", row)>90:
                return list_col.index(row)
            elif "retained earnings" in str(row):
                return list_col.index(row)
            elif "retained surplus" in str(row):
                return list_col.index(row)
            elif "deferred liabilities" in str(row):
                return list_col.index(row)
            elif "retained profits" in str(row):
                return list_col.index(row)
            elif "accumulated profits" in str(row):
                return list_col.index(row)
            elif "undistributed profits" in str(row):
                return list_col.index(row)
            elif "undivided profits" in str(row):
                return list_col.index(row)
            elif "earned surplus" in str(row):
                return list_col.index(row)
    
    def share_capital(list_col):
        
        for row in list_col:
            if fuzz.WRatio("share capital", row)>90:
                return list_col.index(row)
            elif "share capital" in str(row):
                return list_col.index(row)
    
    def special_reserve(list_col):
        
        for row in list_col:
            if fuzz.WRatio("special reserves", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("other reserve", row)>90:
                return list_col.index(row)
            elif "special reserve" in str(row):
                return list_col.index(row)
            elif "other reserve" in str(row):
                return list_col.index(row)
            
     
    def total_equity_and_liablities(list_col):
        
        for row in list_col:
            if fuzz.WRatio("total equity and liabilities", row)>95:
                return list_col.index(row)
            elif fuzz.WRatio("total equity & liabilities", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("total liabilities and equity", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("total liabilities & equity", row)>90:
                return list_col.index(row)
            elif "total equity and liabilities" in str(row):
                return list_col.index(row)
            elif "total equity & liabilities" in str(row):
                return list_col.index(row)
            elif "total liabilities and equity" in str(row):
                return list_col.index(row)
            elif "total liabilities & equity" in str(row):
                return list_col.index(row)
    
    def convertible_debts(list_col):
        
        for row in list_col:
            if fuzz.WRatio("Convertable Debts", row)>95:
                return list_col.index(row)
            elif fuzz.WRatio("Convertable Bonds", row)>90:
                return list_col.index(row)
            elif "convertable debts" in str(row):
                return list_col.index(row)
            elif "convertable bonds" in str(row):
                return list_col.index(row)
    
    def longterm_assets(list_col):
        
        for row in list_col:
            if fuzz.WRatio("longterm assets", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("longterm financial assets", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("longterm insurence", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("longterm advances", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("longterm loans", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("longterm loans and advances", row)>90:
                return list_col.index(row)
            elif "longterm assets" in str(row):
                return list_col.index(row)
            elif "longterm insurence" in str(row):
                return list_col.index(row)
            elif "longterm advances" in str(row):
                return list_col.index(row)
            elif "longterm financial assets" in str(row):
                return list_col.index(row)
            elif "longterm loans" in str(row):
                return list_col.index(row)
            elif "longterm loans and advances" in str(row):
                return list_col.index(row)
    
    
    def longterm_liabilities(list_col):
        
        for row in list_col:
            if fuzz.WRatio("longterm debts", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("longterm financial debts", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("longterm bonds", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("longterm provisions", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("longterm borrowings", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("longterm liabilities", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("longterm policyholder liabilities", row)>90:
                return list_col.index(row)
            elif "longterm debts" in str(row):
                return list_col.index(row)
            elif "longterm borrowings" in str(row):
                return list_col.index(row)
            elif "longterm liabilities" in str(row):
                return list_col.index(row)
            elif "longterm bonds" in str(row):
                return list_col.index(row)
            elif "longterm provisions" in str(row):
                return list_col.index(row)
            
    cash_and_cash_equivalent_row = cash_and_cash_equivalent(list_col)
    account_receivables_row = account_receivables(list_col)
    inventory_row = inventory(list_col)
    property_plant_and_equipment_row = property_plant_and_equipment(list_col)
    intangible_assets_row = intangible_assets(list_col)
    total_assets_row = total_assets(list_col)
    account_payable_row = account_payable(list_col)
    deferred_revenue_row = deferred_revenue(list_col)
    total_liabilities_row = total_liabilities(list_col)
    total_equity_row = total_equity(list_col)
    retained_earnings_row = retained_earnings(list_col)
    share_capital_row = share_capital(list_col)
    special_reserve_row = special_reserve(list_col)
    total_equity_and_liablities_row = total_equity_and_liablities(list_col)
    convertible_debts_row = convertible_debts(list_col)
    longterm_assets_row = longterm_assets(list_col)
    longterm_liabilities_row = longterm_liabilities(list_col)
    
    line_items = {}
    
    if cash_and_cash_equivalent_row != None:
        line_items["cash_and_cash_equivalent"] = list_col[cash_and_cash_equivalent_row]
        
    else:
        line_items["cash_and_cash_equivalent"] = "Not Found"
        
    if account_receivables_row != None:
        line_items["account_receivables"] = list_col[account_receivables_row]
        
    else:
        line_items["account_receivables"] = "Not Found"
        
    if inventory_row != None:
        line_items["inventory"] = list_col[inventory_row]
        
    else:
        line_items["inventory"] = "Not Found"
    
    if property_plant_and_equipment_row != None:
        line_items["property_plant_and_equipment"] = list_col[property_plant_and_equipment_row]
        
    else:
        line_items["property_plant_and_equipment"] = "Not Found"
        
    if intangible_assets_row != None:
        line_items["intangible_assets"] = list_col[intangible_assets_row]
        
    else:
        line_items["intangible_assets"] = "Not Found"
        
    if total_assets_row != None:
        line_items["total_assets"] = list_col[total_assets_row]
        
    else:
        line_items["total_assets"] = "Not Found"
        
    if account_payable_row != None:
        line_items["account_payable"] = list_col[account_payable_row]
        
    else:
        line_items["account_payable"] = "Not Found"
        
    if deferred_revenue_row != None:
        line_items["deferred_revenue"] = list_col[deferred_revenue_row]
        
    else:
        line_items["deferred_revenue"] = "Not Found"
        
    if total_liabilities_row != None:
        line_items["total_liabilities"] = list_col[total_liabilities_row]
        
    else:
        line_items["total_liabilities"] = "Not Found"
        
    if total_equity_row != None:
        line_items["total_equity"]= list_col[total_equity_row]
        
    else:
        total_equity = "Not Found"
        
    if retained_earnings_row != None:
        line_items["retained_earnings"] = list_col[retained_earnings_row]
        
    else:
        line_items["retained_earnings"] = "Not Found"
        
    if share_capital_row != None:
        line_items["share_capital"] = list_col[share_capital_row]
        
    else:
        line_items["share_capital"] = "Not Found"
        
    if special_reserve_row != None:
        line_items["special_reserve"] = list_col[special_reserve_row]
        
    else:
        line_items["special_reserve"]  = "Not Found"
        
    if total_equity_and_liablities_row != None:
        line_items["total_equity_and_liablities"] = list_col[total_equity_and_liablities_row]
        
    else:
        line_items["total_equity_and_liablities"] = "Not Found"
    
    if convertible_debts_row != None:
        line_items["convertible_debts"] = list_col[convertible_debts_row]
        
    else:
        line_items["convertible_debts"] = "Not Found"
    if longterm_assets_row != None:
        line_items["longterm_assets"] = list_col[longterm_assets_row]
        
    else:
        line_items["longterm_assets"] = "Not Found"
        
    if longterm_liabilities_row != None:
        line_items["longterm_liabilities"] = list_col[longterm_liabilities_row]
        
    else:
        line_items["longterm_liabilities"] = "Not Found"
        
        
        
    return line_items