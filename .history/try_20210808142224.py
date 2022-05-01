
#default paramters
def my_function(string1, string2="goodbye"): #第二个param可选输入或不输入
  return string1 + " " + string2

print(my_function("hello", "world")) #prints hello world，输入就按输入的
print(my_function("Time for")) #prints Time for goodbye，没输入就按default


def positional_and_default(p1, p2, p3="a", p5=1, p6=None):
    #positional parameters:p1, p2; 放最前；必须有
    #default parameters：p3="a", p5=1, p6=None； 放后面；可以没有
    #如果只有default parameters，这funct就相当于不需要parameter
    
    #可以通过name和position来引用parameter，或者修改覆盖parameter
    pass


