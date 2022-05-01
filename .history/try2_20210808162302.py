
def square(n=None, s=None): #“None” as a special default value用于判断是否传入想要的参数
    if (n is not None):
        return n * n
    elif (s is not None 
            and isinstance(s, str) 
            and s.isnumeric()):
        return int(s) * int(s)
    else: 
        return None # should throw an Error really...
    
print(square(n=4))
print(square(s="4"))
print(square(s="Hello"))

