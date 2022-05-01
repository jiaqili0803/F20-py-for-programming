
#default paramters
def my_function(string1, string2="goodbye"): #第二个param可选输入或不输入
  return string1 + " " + string2

print(my_function("hello", "world")) #prints hello world，输入就按输入的
print(my_function("Time for")) #prints Time for goodbye，没输入就按default




