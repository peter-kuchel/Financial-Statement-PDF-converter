import readdocs as rd 
import sortdata  
import time 


DOC_NAME = "TD_test.do"
sheets_to_find = ["CONSOLIDATED BALANCE SHEET", "CONSOLIDATED STATEMENT OF INCOME", "CONSOLIDATED STATEMENT OF CASH FLOWS"]
TEXT_DOC = DOC_NAME.replace(".do",".txt")

if __name__ == "__main__":

    #calc start time
    # start = time.time()

    #READ PDF
    # pdfProcess = rd.pdfReader(DOC_NAME, sheets_to_find)
    # sheets_dict = pdfProcess.compile_sheets()
    # sheets_list = sortdata.sort_into_sheets(sheets_dict, sheets_to_find)
    # print(sheets_list[0]) 

    #OPEN TEST
    with open("TD_test.txt", 'r') as test_doc:
        sheets_list = test_doc.read().split('\n') 
    test_doc.close()

    # 0 is balance sheet 
    # 1 is income statement
    # 2 is cash flows statement 

    cleaned_sheets = [sortdata.sort_and_define_items(x) for x in sheets_list]

    #to format the sheets to be exported to excel 
    sortdata.sort_sheet_items(cleaned_sheets)





    #sorted_items = list(map(lambda x: sortdata.sort_and_define_items(x), sheets_list))
    #sortdata.create_text_file(DOC_NAME, sheets_dict) 

    #calc end time 
    # end = time.time()
    # print(end-start)
