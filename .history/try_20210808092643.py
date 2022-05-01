s = 'this is my superduper short sentcence'
count = 0
def num_short_words(sentence):
    for i in sentence.split():
        if len(i) < 5:
            count = count + 1
        print(count)
        
    




print(num_short_words(s)) #print 3

    
