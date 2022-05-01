
def incr(n, amt=1):
    if n == 7:
        return 'bingo'
    
    n = n + amt
    return n
    
    
print('ok')
print(incr(5))
print(incr(5,amt=2))
print(incr(4))
