s = 'this is my superduper short sentcence'

def num_short_words(sentence):
    count = 0
    for i in sentence.split():
        if len(i) < 5:
            count = count + 1
    return count
        
    




print(num_short_words(s)) #print 3

    
