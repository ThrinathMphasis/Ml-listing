# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 16:23:14 2021

@author: thrinath.nelaturi
"""

from fuzzywuzzy import fuzz 


def get_profit_and_loss_direct_line_items(page_content):
    page_content = page_content.lower()
    paragraphs = page_content.split("\n\n")
    all_lines = []
    for para in paragraphs:
        lines = para.split("\n")
        for k in lines:
            all_lines.append(k)
    
    list_col = all_lines
    
    def net_revenue(list_col):
           
        for row in list_col:
            if fuzz.WRatio("net revenue", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("revenue", row)>95:
                return list_col.index(row)
            elif fuzz.WRatio("Net forwarding revenue", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("total income", row)>90:
                return list_col.index(row)
            elif "net revenue" in str(row):
                return list_col.index(row)
            elif "total income" in str(row):
                return list_col.index(row)
    
    
    def Cost_of_goods(list_col):
        for row in list_col:
            if fuzz.WRatio("Cost of goods", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("cost of materials", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("cost of materials consumed", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("cost of sales", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("cost of goods and sales", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("COGS", row)>90:
                return list_col.index(row)
            elif "cogs" in str(row):
                return list_col.index(row)
            elif "cost of goods" in str(row):
                return list_col.index(row)
            elif "cost of sales" in str(row):
                return list_col.index(row)
            elif "cost of materials" in str(row):
                return list_col.index(row)
            
            
    def gross_profit(list_col):
            
        for row in list_col:
            if fuzz.WRatio("Gross profit", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("Net profit", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("Profit for the year", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("work in progress", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("finished product", row)>90:
                return list_col.index(row)
            elif "gross profit" in str(row):
                return list_col.index(row)
            elif "net profit" in str(row):
                return list_col.index(row)
            elif "finished product" in str(row):
                return list_col.index(row)
            elif "profit for the year" in str(row):
                return list_col.index(row)
    
    def salary_expense(list_col):
            
        for row in list_col:
            if fuzz.WRatio("personnel expenses", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("salary expense", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("Employee benefits expenses", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("Employee benefits", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("Employees Expenses", row)>90:
                return list_col.index(row)
            elif "personnel expenses" in str(row):
                return list_col.index(row)
            elif "employee benefits" in str(row):
                return list_col.index(row)
            elif "employees expenses" in str(row):
                return list_col.index(row)
            elif "salary" in str(row):
                return list_col.index(row)
    
    
    
    def tax_expense(list_col):
            
        for row in list_col:
            if fuzz.WRatio("Tax expense", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("Income tax expenses", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("Income taxes", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("Tax expense", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("Income taxes paid", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("Tax expense", row)>90:
                return list_col.index(row)
            elif "income tax" in str(row):
                return list_col.index(row)
            elif "tax expense" in str(row):
                return list_col.index(row)
    
    def operating_expenses(list_col):
        
        for row in list_col:
            if fuzz.WRatio("operating expenses", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("Total operating expenses", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("Net cash from operating activities", row)>90:
                return list_col.index(row)
            elif "operating" in str(row):
                return list_col.index(row)
            elif "operating activities" in str(row):
                return list_col.index(row)
            elif "operating expenses" in str(row):
                return list_col.index(row)
    
    
    def general_and_administrative_expenses(list_col):
        
        for row in list_col:
            if fuzz.WRatio("general and administrative expenses", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("administrative expenses", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("general expenses", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("rent", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("utilities", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("insurence", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("Executives wages and benefits", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("office fixtures and equipment", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("Office supplies", row)>90:
                return list_col.index(row)
            elif "office fixtures" in str(row):
                return list_col.index(row)
            elif "insurence" in str(row):
                return list_col.index(row)
            elif "utilities" in str(row):
                return list_col.index(row)
            elif "office supplies" in str(row):
                return list_col.index(row)
            elif "general expenses" in str(row):
                return list_col.index(row)
            elif "administrative expenses" in str(row):
                return list_col.index(row)
    
    
    def operating_result_EBIT(list_col):
        
        for row in list_col:
            type(row)
            if fuzz.WRatio("operating result", row)>90:
                return list_col.index(row)
            
            elif "ebit" in str(row):
                return list_col.index(row)
            elif "deferred revenue" in str(row):
                return list_col.index(row)
            
    
    def EBITDA(list_col):
        for row in list_col:
            if fuzz.WRatio("ebitda", row)>95:
                return list_col.index(row)
            elif "ebitda" in str(row):
                return list_col.index(row)
    
    def depreciation(list_col):
            
        for row in list_col:
            if fuzz.WRatio("depreciation", row)>90:
                return list_col.index(row)
            elif "depreciation" in str(row):
                return list_col.index(row)
                 
    def amortization(list_col):
            
        for row in list_col:
            if fuzz.WRatio("Amortization", row)>90:
                return list_col.index(row)
            elif "amortization" in str(row):
                return list_col.index(row)
            
    def impairment(list_col):
            
        for row in list_col:
            if fuzz.WRatio("Impairment", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("goodwill Impairment", row)>90:
                return list_col.index(row)
            elif "impairment" in str(row):
                return list_col.index(row)
    
    def stock_based_compensation(list_col):
             
        for row in list_col:
            if fuzz.WRatio("Stock Based Compensation", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("Stock Compensation", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("equity compensation", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("share based compensation", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("share compensation", row)>90:
                return list_col.index(row)
            elif "stock Compensation" in str(row):
                return list_col.index(row)
            elif "share compensation" in str(row):
                return list_col.index(row)
            elif "equity compensation" in str(row):
                return list_col.index(row)
    
    def sales_and_marketing_expense(list_col):
             
        for row in list_col:
            if fuzz.WRatio("Sales and Marketing Expense", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("Marketing Expense", row)>90:
                return list_col.index(row)
            elif fuzz.WRatio("Sales Expense", row)>90:
                return list_col.index(row)
            
            elif "marketing expense" in str(row):
                return list_col.index(row)
            elif "sales expense" in str(row):
                return list_col.index(row)
            
            
    net_revenue_row = net_revenue(list_col)
    Cost_of_goods_row = Cost_of_goods(list_col)
    gross_profit_row = gross_profit(list_col)
    salary_expense_row= salary_expense(list_col)
    tax_expense_row = tax_expense(list_col)
    operating_expenses_row = operating_expenses(list_col)
    operating_result_EBIT_row = operating_result_EBIT(list_col)
    EBITDA_row = EBITDA(list_col)
    depreciation_row = depreciation(list_col)
    amortization_row = amortization(list_col)
    impairment_row = impairment(list_col)
    stock_based_compensation_row = stock_based_compensation(list_col)
    sales_and_marketing_expense_row = sales_and_marketing_expense(list_col)
    
    
    line_items = {}
    
    if net_revenue_row != None:
        line_items["net_revenue"] = list_col[net_revenue_row]
        
    else:
        line_items["net_revenue"] = "Not Found"
        
    if Cost_of_goods_row != None:
        line_items["Cost_of_goods"] = list_col[Cost_of_goods_row]
        
    else:
        line_items["Cost_of_goods"] = "Not Found"
        
    if gross_profit_row != None:
        line_items["gross_profit"] = list_col[gross_profit_row]
        
    else:
        line_items["gross_profit"] = "Not Found"
        
    if salary_expense_row != None:
        line_items["salary_expense"] = list_col[salary_expense_row]
        
    else:
        line_items["salary_expense"] = "Not Found"
        
    if tax_expense_row != None:
        line_items["tax_expense"] = list_col[tax_expense_row]
        
    else:
        line_items["tax_expense"] = "Not Found"
        
    if operating_expenses_row != None:
        line_items["operating_expenses"] = list_col[operating_expenses_row]
        
    else:
        line_items["operating_expenses"] = "Not Found"
        
    if operating_result_EBIT_row != None:
        line_items["operating_result_EBIT"] = list_col[operating_result_EBIT_row]
        
    else:
        line_items["operating_result_EBIT"] = "Not Found"
        
    if EBITDA_row != None:
        line_items["EBITDA"] = list_col[EBITDA_row]
        
    else:
        line_items["EBITDA"]  = "Not Found"
        
    if depreciation_row != None:
        line_items["depreciation"] = list_col[depreciation_row]
        
    else:
        line_items["depreciation"] = "Not Found"
        
    if amortization_row != None:
        line_items["amortization"] = list_col[amortization_row]
        
    else:
        line_items["amortization"] = "Not Found"
        
    if impairment_row != None:
        line_items["impairment"] = list_col[impairment_row]
        
    else:
        line_items["impairment"] = "Not Found"
        
    if stock_based_compensation_row != None:
        line_items["stock_based_compensation"] = list_col[stock_based_compensation_row]
        
    else:
        line_items["stock_based_compensation"] = "Not Found"
        
    if sales_and_marketing_expense_row != None:
        line_items["sales_and_marketing_expense"] = list_col[sales_and_marketing_expense_row]
        
    else:
        line_items["sales_and_marketing_expense"] = "Not Found"
        
    return line_items
        