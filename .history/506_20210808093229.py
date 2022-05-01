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
def count_values(the_dict):
    count = {}
    for i in the_dict.values():
        count[i] = count.get(i,0) + 1
    return count

values = {'a':8, 'b':2, 'c':7, 
          'd':14, 'e':17, 'f':8, 
          'g':7, 'h':8, 'i':14}
value2 = {}
value3 = {'a':'apple', 'b':'banana', 'c':'apple'}

print(count_values(values))
print(count_values(value2))
print(count_values(value3))

#9
list_of_dicts = [{'a':1,'b':2,"d":11}, 
                 {'a':4,'b':5,"d":12}, 
                 {'a':7,'b':8,"d":11}]

def values_of_d(dict_list):
    d_list = []
    for i in dict_list:
        d_list.append(i['d'])
    return d_list
        
print(values_of_d(list_of_dicts))

#10
pokemon_go_data = [
    {
    'Rattata':203, 'b':2, 'c':7, 
    'd':14, 'e':17, 'f':8, 
    'g':7, 'h':8, 'i':14
    },   
    {
    'a':8, 'Rattata':245, 'c':7, 
    'd':14, 'e':17, 'f':8, 
    'g':7, 'h':8, 'i':14
    },
    {
    'Rattata':32,  'c':7, 
    'd':14, 'e':17, 'f':8, 
    'g':7, 'h':8, 'i':14
    },
    {
    'a':8,  'Rattata':107, 
    'd':14, 'e':17, 'f':8, 
    'g':7, 'h':8, 'i':14
    }
]

candy_count = {}
for dict in pokemon_go_data:
    
    for key in dict.keys():
        
        if key not in candy_count:
            candy_count[key] = dict[key]
            
        else:
            candy_count[key] += dict[key]
    
most_candied_pokemon = list(candy_count.keys())[0]
for pokemon in candy_count.keys():

    if candy_count[pokemon] > candy_count[most_candied_pokemon]:
        most_candied_pokemon = pokemon

print(most_candied_pokemon)

#11
cars = [
    {'name':'exploer', 'marker':'ford', 'price':34104},   
    {'name':'bolt', 'marker':'cglevrolet', 'price':37495}, 
    {'name':'camry', 'marker':'toyota', 'price':25380}, 
    {'name':'civic', 'marker':'honda', 'price':20805}
]

carprices = {}

for c in cars:
    n = c['name']
    p = c['price']
    carprices[n] = p  
    
print(carprices)

#12
s = 'this is my superduper short sentcence'

def num_short_words(sentence):
    count = 0
    for i in sentence.split():
        if len(i) < 5:
            count = count + 1
    return count
        
print(num_short_words(s)) #print 3

#13
a_list = [1,2]
other_list = [5,6,7,8]

a_list += [3,4]

final_list = a_list[3:]+other_list[:3]
print(final_list)   #4567

#14
