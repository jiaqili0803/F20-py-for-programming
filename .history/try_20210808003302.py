def wrod_counts(s):
    d = {}
    words = s.split()
    for w in words:
        if w in d:
            d[w] = d[w] + 1
        else:
            d[w] = 1
        return d

print(word_conts('a man a plan a canal, Panama'))
    