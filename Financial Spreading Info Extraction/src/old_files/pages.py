from relevent_pages import extract as relevent_pages_def
from get_dates import get_dates
from balance_sheet_fields import get_balance_sheet_line_items
from cash_flow_fields import get_cash_flow_direct_line_items
from profit_and_loss_fields import get_profit_and_loss_direct_line_items

#filepath = "Input/fm global.pdf"
def match_correct_page(pages):
    relevent_pages_original = list(set(pages))
    relavent_pages = []
    for page in relevent_pages_original:
        relavent_pages.append(page-1)
        
    relavent_pages = list(set(relavent_pages))
    return relavent_pages

def add_one(a):
    return [x + 1 for x in a]

def get_selected_content(content,pages):
    return [content[i-1] for i in pages]

def get_pages(filepath):
    
    content,relevent_page_numbers_balance_sheet, relevent_page_numbers_cash_flow, relevent_page_numbers_profit_loss = relevent_pages_def(filepath)
    
    # relevent_page_numbers_balance_sheet = match_correct_page(relevent_page_numbers_balance_sheet)
    # relevent_page_numbers_cash_flow = match_correct_page(relevent_page_numbers_cash_flow)
    # relevent_page_numbers_profit_loss = match_correct_page(relevent_page_numbers_profit_loss)
    
    # relevent_page_numbers_balance_sheet = add_one(relevent_page_numbers_balance_sheet)
    # relevent_page_numbers_cash_flow = add_one(relevent_page_numbers_cash_flow)
    # relevent_page_numbers_profit_loss = add_one(relevent_page_numbers_profit_loss)
    
    
    #complete_pages = list(set(relevent_page_numbers_balance_sheet+relevent_page_numbers_cash_flow+relevent_page_numbers_profit_loss))
    
    Dict = {} 
    #Dict['complete_pages'] = {} 
    Dict['balance_sheet'] = {}
    Dict['cash_flow'] = {}
    Dict['profit_loss'] = {}
        
    # if complete_pages !=[]:
    #     for page in complete_pages:
    #         Dict['complete_pages']["page.No:"+str(page)] = content[page - 1 ]
            
    # else:
    #     Dict['complete_pages']= {}

    if relevent_page_numbers_balance_sheet !=[]:
        for page in relevent_page_numbers_balance_sheet:
            #page = 191
            mini_dict = {}
            mini_dict['Content']= content[page - 1]
            mini_dict['sub-fields'] = get_balance_sheet_line_items(content[page - 1])
            mini_dict['Years'] = get_dates(content[page - 1])
            Dict['balance_sheet']["page.No:"+str(page)] = mini_dict
            #Dict['balance_sheet']["Year:"] = 0 
    else:
        Dict['balance_sheet']= {}
        
    
    if relevent_page_numbers_cash_flow !=[]: 
        for page in relevent_page_numbers_cash_flow:
            mini_dict = {}
            mini_dict['Content']= content[page - 1]
            mini_dict['sub-fields'] = get_cash_flow_direct_line_items(content[page - 1])
            mini_dict['Years'] = get_dates(content[page - 1])
            Dict['cash_flow']["page.No:"+str(page)] = mini_dict
            #Dict['cash_flow']["Year:"] = 0
    else:
        Dict['cash_flow']= {}
    
    
    if relevent_page_numbers_profit_loss !=[]:
        for page in relevent_page_numbers_profit_loss:
            mini_dict = {}
            mini_dict['Content']= content[page - 1]
            mini_dict['sub-fields'] = get_profit_and_loss_direct_line_items(content[page - 1])
            mini_dict['Years'] = get_dates(content[page - 1])
            Dict['profit_loss']["page.No:"+str(page)] = mini_dict
            #Dict['profit_loss']["Year:"] = 0
    else:
        Dict['profit_loss']= {}
        
   
    return Dict