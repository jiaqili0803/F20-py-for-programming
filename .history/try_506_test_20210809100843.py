def word_counts(s):
    d = {}
    words = s.split()
    for w in words:
        if w not in d:
            d[w] = d[w] + 1
        else:
            d[w] = 1
    return d

print(word_counts("a man a plan a canal, Panama"))