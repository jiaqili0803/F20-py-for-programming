#1
dict = {}
def do_letter_counts(s, chars_to_count):
    for i in s:
        if i in chars_to_count:
            dict[i] = dict.get(i,0) + 1
    return print(dict)
            
do_letter_counts('hello', ['l','o'])

#2
person = 'Sarah Smith '
thing = 'likes to swim.'
print(person + thing)

#3
item = 'new book'
price = 12

price = str(price)
print('My '+ item +' cost $'+price+'.')

#4

