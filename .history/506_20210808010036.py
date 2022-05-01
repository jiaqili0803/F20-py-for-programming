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
x = 20

if x > 30:
    if x < 40:
        print('Big')
    else:
        print('Very big')   
elif x >= 26:
    print('small')   
else:
    print('very small')
    
#5
def word_counts(s):
    d = {}
    words = s.split()
    print(words)

    for w in words:
        if w in d:
            d[w] = d[w] + 1
        else:
            d[w] = 1
    return d
print(word_counts('a man a plan a canal, Panama'))

#6
def incr(n, amt=1):
    
    n = n + amt
    
    if n == 7:
        return 'bingo' #return出去了就不回来了，一次fuct只return一个东西
    
    print('ok')
    return n

print(incr(5))
print(incr(5,amt=2))
print(incr(4))

#7
b = 12
while True:
    print('B')
    b += 2
    if b > 15:
        break
    
#8
