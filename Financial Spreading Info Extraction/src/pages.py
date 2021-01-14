from relevent_pages import extract as relevent_pages_def
from get_dates import get_dates
from balance_sheet_fields import get_balance_sheet_line_items
from cash_flow_fields import get_cash_flow_direct_line_items
from profit_and_loss_fields import get_profit_and_loss_direct_line_items

def get_pages(filepath):
    print("2")
    content,relevent_page_numbers_balance_sheet, relevent_page_numbers_cash_flow, relevent_page_numbers_profit_loss = relevent_pages_def(filepath)
    
    Dict = {}
     
    Dict['balance_sheet'] = {}
    Dict['cash_flow'] = {}
    Dict['profit_loss'] = {}
    
    if relevent_page_numbers_balance_sheet !=[]:
        for page in relevent_page_numbers_balance_sheet:
            mini_dict = {}
            mini_dict['Content']= content[page - 1]
            mini_dict['sub-fields'] = get_balance_sheet_line_items(content[page - 1])
            mini_dict['Years'] = get_dates(content[page - 1])
            Dict['balance_sheet']["page.No:"+str(page)] = mini_dict
            
    else:
        Dict['balance_sheet']= {}
    
    if relevent_page_numbers_cash_flow !=[]: 
        for page in relevent_page_numbers_cash_flow:
            mini_dict = {}
            mini_dict['Content']= content[page - 1]
            mini_dict['sub-fields'] = get_cash_flow_direct_line_items(content[page - 1])
            mini_dict['Years'] = get_dates(content[page - 1])
            Dict['cash_flow']["page.No:"+str(page)] = mini_dict
            
    else:
        Dict['cash_flow']= {}
    
    if relevent_page_numbers_profit_loss !=[]:
        for page in relevent_page_numbers_profit_loss:
            mini_dict = {}
            mini_dict['Content']= content[page - 1]
            mini_dict['sub-fields'] = get_profit_and_loss_direct_line_items(content[page - 1])
            mini_dict['Years'] = get_dates(content[page - 1])
            Dict['profit_loss']["page.No:"+str(page)] = mini_dict
            
    else:
        Dict['profit_loss']= {}
    
    return Dict
