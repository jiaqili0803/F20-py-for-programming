
dict = {}
def do_letter_counts(s, chars_to_count):
    for i in s:
        if i in chars_to_count:
            dict[i] = dict.get(i,0) + 1
    
        
    
    
    
    
    
    
    
    
do_letter_counts('hello', ['l','o'])
