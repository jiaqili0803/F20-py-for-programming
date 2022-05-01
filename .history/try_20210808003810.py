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
    