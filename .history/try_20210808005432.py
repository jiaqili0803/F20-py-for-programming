
def incr(n, amt=1):
    
    n = n + amt
    
    if n == 7:
        return 'bingo' #return出去了就不回来了，一次fuct只return一个东西
    
    print('ok')
    return n
    
    

print(incr(5))
print(incr(5,amt=2))
print(incr(4))
