import io 
import re
from time import sleep 
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage 

class pdfReader:
    def __init__(self, pdf_file, sheets_to_find):
        self.pdf_file = pdf_file
        self.sheets_to_find = sheets_to_find
        self.INCASE_INCOME_FIND = "CONSOLIDATED STATEMENTS OF COMPREHENSIVE INCOME"

    #this is to process the PDF and returns a list of the pages in the specified range 
    def process_PDF_to_text(self, checkRange):
        with open(self.pdf_file, 'rb') as FNCE_PDF:
                all_pages = [page for page in PDFPage.get_pages(FNCE_PDF, maxpages= checkRange, caching= True, check_extractable= True)]
                full_PDF_text = []
                for page in all_pages:
                    resource_manager = PDFResourceManager()
                    file_handler = io.StringIO()
                    converter = TextConverter(resource_manager, file_handler)
                    page_interpreter = PDFPageInterpreter(resource_manager, converter)
                    page_interpreter.process_page(page)
                    just_text = file_handler.getvalue()
                    full_PDF_text.append(just_text)
        converter.close()
        file_handler.close()
        return full_PDF_text

    #find the cashflow sheet as this is usually the last of the 3 sheets
    def find_end(self, first_text_list, look_range):
        cash_flows = self.sheets_to_find[-1]
        for text in first_text_list:
            match_ob = re.search(cash_flows, text[:look_range].upper())
            if match_ob != None:
                print(f"End position found at page: {first_text_list.index(text)+1}")
                return first_text_list.index(text)
        return None 

    #loops to find the last sheet position in the pdf document
    #
    def initial_find_end_positions(self):
        last_position_found = False
        look_range = 40
        check = 10 #first number of sheets to start looking at
        print("Searching for end position")
        while last_position_found == False:
            find_attempt = self.process_PDF_to_text(check) 
            position_search = self.find_end(find_attempt, look_range)
            if position_search != None:
                last_position_found = True
            else:
                print("Extending search range...")
                check += 2 #look at another sheet if the cash-flows sheet is not found
                look_range += 5
        return find_attempt[:position_search+1] #return the text up to where the cash flows sheet was found

    def find_financial_sheets(self, text_list, look_range):
        financial_statements = {}
        for text in text_list:
            for name in self.sheets_to_find:
                match_ob  = re.search(name, text[:look_range].upper())
                if match_ob != None:
                    financial_statements[name] = text
        return financial_statements
    
    #main sheet finder
    def compile_sheets(self):
        print("Now finding sheets")
        look_range = 60
        sheets_compiled = False

        #will look for range with all sheets before 
        processed_text = self.initial_find_end_positions()
        count = 0
        while sheets_compiled == False:
            sheets_found = self.find_financial_sheets(processed_text, look_range)
            if len(sheets_found.keys()) == 3:
                sheets_compiled = True
            else:
                print("Still searching for sheets...")
                if count == 2:
                    self.sheets_to_find.append(self.INCASE_INCOME_FIND) 
                look_range += 5
                count += 1
        print("Sheets found")
        return sheets_found 
            