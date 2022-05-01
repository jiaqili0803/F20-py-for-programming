'''
- Default and named parameters
    - A review(?)
    - Beware the mutable default parameter!
- Constructing objects from JSON
    - Using default and named parameters to support constructor overloading
- A brief introduction to unit testing (just enough for Project 1)
'''

#default paramters
def my_function(string1, string2="goodbye"): #第二个param可选输入或不输入
    return string1 + " " + string2
print(my_function("hello", "world")) #prints hello world，输入就按输入的
print(my_function("Time for")) #prints Time for goodbye，没输入就按default

def positional_and_default(p1, p2, p3="a", p5=1, p6=None):
    pass
    #positional parameters:p1, p2; 放最前；必须有
    #default parameters：p3="a", p5=1, p6=None； 放后面；可以没有
    #如果只有default parameters，这funct就相当于不需要parameter
    
#可以通过name和position来引用、修改覆盖parameter（有position parameter必须在前；只利用name改，无所谓顺序）
def many_params(p1=1, p2=2, p3=3, p4=4):
    return p1 + p2 + p3 + p4

print(many_params())   #prints 10; 没更改
print(many_params(2, 4, 6, 8))  #prints 20； 利用position改
print(many_params(p4=10))  #prints 16； 利用name改
print(many_params(30, p3=40))  #prints 76； 用position改了第一位的，name改了p3
print(many_params(p3=3, p1=6))  #prints 15；只利用name改，无所谓顺序
 
#default paramters在class中作用：避免有object缺parameter但是还能call
