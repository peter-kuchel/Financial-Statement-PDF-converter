import re 

class cleanSheets:
    def __init__(self, sheet_text):
        self.sheetText = ' '.join(sheet_text.split())
        self.no_notes = True 
        self.just_numbers = re.compile('[0123456789]')
        self.just_upper = re.compile('[A-Z]')
    
    def remove_irregularities(self):
        note_pattern = re.compile(r'(\(note+[^)]*\))', flags= re.IGNORECASE) #to find the: (notes) in the text
        hypen_pattern = re.compile(r'\s+[–]+\s') #to remove hypens when spliting the text up
        note_matches = note_pattern.findall(self.sheetText) 
        if note_matches != []:
            self.sheetText = note_pattern.sub("", self.sheetText)
        else:
            self.no_notes = False 
        self.sheetText = self.sheetText.replace('$', "") 
        self.sheetText = hypen_pattern.sub(' ', self.sheetText)
    
    def remove_bottom_text(self):
        limit_phrase_bottom = 'The accompanying' #at the bottom of all sheets 
        self.sheetText = self.sheetText.split(limit_phrase_bottom)[0] #can also use re for spliting this if needed 
    
    def return_filtered_text(self):
        return (self.sheetText, self.no_notes)


        # bottom_not_removed = False
        # while bottom_not_removed == False: 
        #     last_items = [self.items_list[-1], self.items_list[-2]] #last two items 
        #     last_items_fixed = list(map(lambda x: re.sub(',','', x), last_items)) #remove the ',' 
        #     print(last_items_fixed) 
        #     try:
        #         int_of_items = [int(i) for i in last_items_fixed] #test to see if the last items are numbers
        #         bottom_not_removed = True 
        #     except TypeError:



        

        