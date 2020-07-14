import re

def test_re_sub(test_str):
    print(f"Before:\n{test_str}")
    test_str = " ".join(test_str.split())
    notes_patterns = r"\(N.*\)"
    note_complie = re.compile(notes_patterns)
    matches = note_complie.findall(test_str)
    print(f'\n{matches}')
    new_test_str = note_complie.sub("", test_str)
    print(f"\nAfter:\n{new_test_str}")
    
    


if __name__ == '__main__':
    with open("test_re.txt") as re_test:
        example_str = re_test.read()
    re_test.close()
    #print(example_str)
    test_re_sub(example_str)

"""
Attempts:

r'(^\(N.*\)$)' - got nothing 
r'(\(N.*\d\))' - got everything 
r'(\(N*\d\))' - got nothing 
r'(\(N\w*\W*\))' - got nothing 
r'(\(N.*,.*\d\))' - got everything
r'(\(N\w*\d.*\d\))' - got nothing
r"\(N\w.*\W," - got nothing 
"""