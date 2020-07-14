import re 


class extractBalanceSheet:

    def __init__(self, balance_sheet_info):
        self.balance_sheet_text = balance_sheet_info[0]
        self.note_status = balance_sheet_info[1]
        self.just_upper = re.compile('[A-Z]')
        self.just_numbers = re.compile('[0123456789]')
        self.just_lower = re.compile('[a-z]')
        # print(self.balance_sheet_text)
    
    def get_balance_sheet_items(self): 
        split_phrase = re.compile('(assets)(?i)') #the (?i) makes it case sensitive as re.split() doesnt take the IGNORECASE flag 
        self.balance_items = split_phrase.split(self.balance_sheet_text, maxsplit=1)[-1].split() 
        print(self.balance_items)
    
    def combine_entry_names(self, entry_index):
        all_letters = re.compile('[a-z]', flags= re.IGNORECASE)
        #check for the next word
        beg = entry_index + 1

        #create a list for the words in the phrase
        word_elements = [self.balance_items[entry_index]]

        #gather the words in a list and break as soon as the next element is a number
        while True: 
            if all_letters.match(self.balance_items[beg]) != None:
                word_elements.append(self.balance_items[beg])
                beg += 1
            else:
                break 
        #join all the words together into a list 
        account =  [" ".join(word_elements)]

        #index of last word 
        last_word_index = beg

        #loop to find the numbers starting at the first index after the last word 
        #if the next index is not a number then break 
        for i in range(last_word_index, len(self.balance_items)):
            if re.search(self.just_numbers, self.balance_items[i]) != None:
                account.append(self.balance_items[i])
            else:
                break 
        return account
    
    def collect_one_offs(self, full_list):
        one_offs = []
        for i, value in enumerate(full_list):
            if re.match(self.just_upper, full_list[i]) != None:
                if re.match(self.just_upper, full_list[i+1]) != None:
                    one_offs.append(value) 

        return one_offs
    
    def combine_items(self):

        # one_offs = self.collect_one_offs(self.balance_items)
        # for i in one_offs:
        #     print(i)
        # print(full_list)

        self.sorted_list = []
        for i, value in enumerate(self.balance_items):

            #checks to see if the element is uppercase 
            if re.match(self.just_upper, value) != None: 

                # check if index ahead is lowercase                           #check if index ahead is a number
                if (re.match(self.just_lower, self.balance_items[i+1]) != None) or (re.match(self.just_numbers, self.balance_items[i+1]) != None):
                    
                    #print(f"For {full_list[i]}, one index up: {full_list[i+1]}")

                    # check if the element behind is not uppercase 
                    if re.match(self.just_upper, self.balance_items[i-1]) == None: 
                        account_word = self.combine_entry_names(i)
                        self.sorted_list.append(account_word)
                    
                elif re.match(self.just_upper, value) != None: #and re.match(self.just_numbers, full_list[i-1]) != None:
                    self.sorted_list.append([value]) 