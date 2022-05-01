## Writing Good Functions
    #use clear names (long and clear is better than short and cryptic)
        #Find-and-replace function、refactor commands来全部替换名称
    #The Single Responsibility Rule
        #一个funct就做一件事，可以分别多分几个funct达成目的，更简洁
        #def compute_average(num_list):   
        #def calculate_student_averages(students, grades): 
        #def find_student_with_highest_average(students, grades):
    #Keep a Function Short（<50 lines）
    #Avoid Side Effects
        #changes should be restricted to the function’s return value
        #are not expected to modify the inputs
    #   
        #不影响外部的任何数据（通过 return 除外），也不应访问其外部的任何数据，例如全局变量（通过其参数除外）
    #document your functions