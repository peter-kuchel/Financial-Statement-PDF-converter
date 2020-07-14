from cleansheets import cleanSheets
from extractBalance import extractBalanceSheet 

def create_text_file(REF_filename, sheets_dict):
    REF_filename = REF_filename.replace(".do", "")+ ".txt"
    text_file = open(REF_filename, 'w')
    for key in sheets_dict.keys():
        text_file.write(sheets_dict[key])
        text_file.write("\n")
    text_file.close()
    # for key in sheets_dict.keys():
    #     save_as_file = REF_filename + str(key) + ".txt"
    #     text_file = open(save_as_file, 'w')
    #     text_file.write(sheets_dict[key])
    #     text_file.close()
    print("Finished")

def sort_and_define_items(sheet):
    sheetClean = cleanSheets(sheet)
    sheetClean.remove_irregularities()
    sheetClean.remove_bottom_text() 
    return sheetClean.return_filtered_text()

def sort_sheet_items(sheets_list):
    balance_sheet = sheets_list[0]
    # income_sheet = sheets_list[1]
    # cashflows_sheet = sheets_list[2]

    #first for balancesheet  
    balance_sheet_sort = extractBalanceSheet(balance_sheet)
    balance_sheet_sort.get_balance_sheet_items()

def sort_into_sheets(sheets_dict, names):
    return [sheets_dict[names[0]], sheets_dict[names[1]], sheets_dict[names[2]]] 

def simplify_dict(text_extract):
    SHEET_ID =["BALANCE", "INCOME", "CASH FLOWS"]
    if type(text_extract) == list:
        return {j:i for j in SHEET_ID for i in text_extract if j in i[:70]}
    else:
        return {j:text_extract[v] for j in SHEET_ID for v in text_extract.keys() if j in text_extract[v][:70]} 
