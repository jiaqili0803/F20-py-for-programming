
def incr(n, amt=1):
   
    n = n + amt
    if n == 7:
        return 'bingo'
    return n
    
    
print('ok')
print(incr(5))
print(incr(5,amt=2))
print(incr(4))
