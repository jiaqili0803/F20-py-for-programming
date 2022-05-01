###Functions make programs more readable
###Functions hide complexity

students = {
    '1001': {'last_name': 'Newman', 'first_name': 'Mark', 'uniqname': 'mwnewman'},
    '1002': {'last_name': 'Kano', 'first_name': 'Tsuyoshi', 'uniqname': 'tkano'},
    '1003': {'last_name': 'Grill', 'first_name': 'Gabriel', 'uniqname': 'ggrill'},
    '1004': {'last_name': 'Chen', 'first_name': 'Kangning', 'uniqname': 'knchen'}
}
grades = {
    '1001': [90, 88, 75, 95],   
    '1002': [92, 99, 88, 100],
    '1003': [95, 88, 82, 100],
    '1004': [99, 92, 94, 98]
}

def find_student_with_highest_average(students, grades):
  max = 0
  max_id = -1
  for id in grades: #循环每个人
      sum = 0
      num_grades = 0
      for g in grades[id]:
          sum += g
          num_grades += 1
      avg = sum/num_grades #每个学生平均分
      if avg > max:
          max = avg
          max_id = id
  return students[max_id] #return平均分最高的学生

top_student = find_student_with_highest_average(students, grades)
print(top_student)


###Functions are reusable-Don’t Repeat Yourself.
# lec2_1.py
students = {
    '1001': {'last_name': 'Newman', 'first_name': 'Mark', 'uniqname': 'mwnewman'},
    '1002': {'last_name': 'Kano', 'first_name': 'Tsuyoshi', 'uniqname': 'tkano'},
    '1003': {'last_name': 'Grill', 'first_name': 'Gabriel', 'uniqname': 'ggrill'},
    '1004': {'last_name': 'Chen', 'first_name': 'Kangning', 'uniqname': 'knchen'}
}

grades = {
    '1001': [90, 88, 75, 95],   
    '1002': [92, 99, 88, 100],
    '1003': [95, 88, 82, 100],
    '1004': [99, 92, 94, 98]
}

#这里可以define一个算average的function，DRY！,被后面几个function重复利用
def compute_average(num_list):
    sum = 0
    num_items = 0
    for n in num_list:
        sum += n
        num_items += 1
    return sum/num_items

def find_student_with_highest_average(students, grades):
    max = 0
    max_id = -1
    for id in grades:
        avg = compute_average(grades[id])
        if avg > max:
            max = avg
            max_id = id
    return students[max_id]

def compute_final_grades(grades):
    student_grades = {}
    for id in grades:
        student_grades[id] = compute_average(grades[id])
    return student_grades

def print_final_grades(students, final_grades):
    for id in final_grades:
        student = students[id]
        print(student['first_name'], student['last_name'], 'has', final_grades[id])

top_student = find_student_with_highest_average(students, grades)
print("The top student is", top_student['first_name'], top_student['last_name'])

final_grades = compute_final_grades(grades)
print_final_grades(students, final_grades)



###Function have scope
#1. Outer scope variables are valid within any inner scopes
var1 = 66 # global scope
def func1():
    print("inside function", var1) # global name is still valid in the function
func1()
print("outside function", var1)
#Prints
>> inside function 66
>> outside function 66

#2. Inner scope variables are not valid in the outer scope
def func3():
    var3 = 99 # local name 
    print("inside function", var3) 
func3()
print("outside function", var3) #inner的到了外面失效
#Prints
>>inside function 99
>>Traceback,NameError: name 'var3' is not defined

#3. local variable overrides a global variable with the same name
var2 = 77 # global scope
def func2():
    var2 = 88 # local name overrides global直接覆盖
    print("inside function", var2)  
func2()
print("outside function", var2)   #外面的还是不受影响
#Prints
>>inside function 88
>>outside function 77



###Function parameters are local variables
def func4(param1):
    print("inside function A", param1)  #inside function A 111
    param1 = 222
    print("inside function B", param1)  #inside function B 222
var4  = 111 #outer variables
func4(var4)
print("outside function", var4)  #outside function 111，outer不受影响

#上下func4、funct5完全一样的结果；
def func5(var5): #parameter这里叫什么都无所谓，重名也不影响，因为作用域不同
    print("inside function A", var5) 
    var5 = 222
    print("inside function B", var5) 
var5  = 111
func5(var5) #call function的时候，相当于把var5这个global variable复制一个到function里面变成local variable去运算
print("outside function", var5) 

def func6(var6):
    var6 += " world"
    print(var6, "from func6") 
var6  = "hello"
func6(var6) #hello world from func6
print(var6, "from indent level 0") #hello from indent level 0


### Immutable types: number types (int, float, long, complex), booleans, strings, tuples. 
#num types just replace to a new one
x = 5
y = x 
print(x) # prints 5
print(y) # prints 5
x = 6 #相当于一个new x
print(x) # prints 6
print(y) # prints 5 还是和旧x值一样，x没有被改变

#str and tuples will hange unsuccessful:
string1 = "I am a string"
string1[3] = "n"  #change unsuccessful
print(string1[3]) #will error
tuple1 = (1, 2, 3)
tuple1[2] = 4 #change unsuccessful
print(tuple1[2]) #will error

#string functions do not change the string,just return a new one
s1 = "hello"
s2 = s1.upper()
print(s1, s2) #hello HELLO

### Mutable types: list, dict
my_list = [1, 2, 3, 4] 
my_list.append(5) # add a new element, changed
print(my_list) # my_list is changed: [1, 2, 3, 4, 5]

my_dict = {'a': 'apple', 'b': 'banana', 'c': 'cherry'}
my_dict['c'] = 'canteloupe'
print(my_dict['c']) #changed: canteloupe

###Pass mutable objects to
#str
s = "hello"
s2 = s 
print(s) # prints "hello"
print(s2) # prints "hello"
s = "world" #相当于一个新s
print(s) # prints "world" 变了
print(s2) # prints "hello"