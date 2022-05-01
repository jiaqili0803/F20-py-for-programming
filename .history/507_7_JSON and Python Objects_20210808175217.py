'''
- Default and named parameters
    - positional parameters: 放最前；必须有
    - default parameters： 放后面；可以没有
    - 可以通过name和position来引用、修改覆盖parameter（有position parameter必须在前；只利用name改，无所谓顺序）
    - default paramters在class中作用：避免有instance的部分parameter不avilible，default可以补上；make sense for all instances of the class
    - #default parameter是 global variable，会被改变并应用到全局！
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
 
 
#default paramters在class中作用：避免有instance的部分parameter不avilible，default可以补上；make sense for all instances of the class
#eg1
class Person:
    def __init__(self, fn="Jane", ln="Doe"):
        self.firstName = fn
        self.lastName = ln

    def full_name(self):
        return self.firstName + " " + self.lastName

people = [
    Person(),  #Jane Doe
    Person("Sam", "Samuelson"), #Sam Samuelson
    Person(ln="Jacobs"), #Jane Jacobs
    Person("John") #John Doe
]

for p in people:
    print(p.full_name())

#eg2
class ClubMember:
    def __init__(self, fn="Jane", ln="Doe", mem_id=-1):
        self.firstName = fn
        self.lastName = ln
        self.member_id = mem_id
        self.is_member = (mem_id != -1) 

    def member_status(self):
        if (self.is_member):
            status = " is "
        else:
            status = " is not "
        return self.firstName + " " + self.lastName + status + "a member"

members = [
    ClubMember(), #Jane Doe is not a member
    ClubMember("Sam", "Samuelson", 1234), #Sam Samuelson is a member
    ClubMember(ln="Jacobs"),  #Jane Jacobs is not a member
    ClubMember("John", mem_id=6666)  #John Doe is a member
]
for m in members:
    print(m.member_status())


#default parameter是 global variable，会被改变并应用到全局！
#eg1
def print_word_list_add_bird(word_list=["dog", "cat", "goat"]):
    print(word_list)
    word_list.append("bird") # 被append后下一次就真的会改变

print_word_list_add_bird()
print_word_list_add_bird()
print_word_list_add_bird()
print_word_list_add_bird()
#will print：
# ['dog', 'cat', 'goat']
# ['dog', 'cat', 'goat', 'bird']
# ['dog', 'cat', 'goat', 'bird', 'bird']
# ['dog', 'cat', 'goat', 'bird', 'bird', 'bird']

#eg2
class Pet:
    def __init__(self, nm, words=["woof", "arf", "yip"]): #default parameter is global variable
        self.name = nm
        self.words = words

    def speak(self):
        my_words = ''
        for w in self.words:
            my_words += w + " "
        return "I can say " + my_words

    def teach(self, new_word):
        self.words.append(new_word) #modified that global variable;所有使用那个default parametr的instance都会被影响

fido = Pet("fido")
rufus = Pet("rufus")
polly = Pet("polly", ["cracker", "pirate", "rrrr"]) #有自己的 不用default parametr的instance，不受影响

print(fido.speak())
fido.teach('ella')
print(rufus.speak())
print(fido.speak())
print(polly.speak())
#print：
# I can say woof arf yip 
# I can say woof arf yip ella 
# I can say woof arf yip ella
# I can say cracker pirate rrrr
 

'''
用 starwars API 创建角色class
'''

#先手动创建两个instance试一下对不对
class Character:

    def __init__(self, nm, sp):
        self.name = nm
        self.species = sp

    def info(self):
        return self.name + " is a " + self.species

luke = Character("Luke Skywalker", "Human")
c3po = Character("C3PO", "Droid")

print(luke.info())
print(c3po.info())

#request 数据from API
import requests

BASE_URL = "https://swapi.dev/api/people" 
resp = requests.get(BASE_URL)
results_object = resp.json() # same as json.loads(resp.text)

people_list = results_object["results"] #把关于人物信息的"results"列表提取

#得到我们想要的
print(people_list[0]) # print the first person in the list
print(people_list[3]['name']) #name and eye color of the fourth person
print(people_list[3]['eye_color']) 
for p in people_list: #print every name
    print(p["name"])


'''
#用default parameter来让python完成类似c++的overloading；
''' 
# 同一funct不同参数 不同情况下返回不同东西
def square(n=None, s=None): 
    #“None” as a special default value用于判断是否传入想要的参数
    if (n is not None):
        return n * n
    elif (s is not None 
            and isinstance(s, str) 
            and s.isnumeric()):
        return int(s) * int(s)
    else: 
        return None 
    
print(square(n=4)) #16
print(square(s="4")) #16
print(square(s="Hello")) #None


'''   
- Constructing objects/multiple class from JSON；举例星球大战API+class 得到我们想要的格式组合的info
##! 另外有两个.py 是详细代码：multiple class
'''
import requests


class Character:
    def __init__(self, nm='', sp='', character_data=None): 
        #character_data=None 则是手动输入的两例情况；else是从API抓下来的info输入进class的情况
        if (character_data is None):
            self.name = nm
            self.species = sp
        else:
            self.name = character_data['name']
            
            if character_data["species"] == []:
                    self.species = "Unknown"
            else:
                if (character_data["species"][0]
                        == "https://swapi.dev/api/species/1/"):
                    self.species = "Human"
                elif (character_data["species"][0]
                        == "https://swapi.dev/api/species/2/"):
                    self.species = "Droid"
                else:
                    self.species = "Unknown"
                
    def info(self):
        return self.name + " is a " + self.species


#### Testing the Character class 用两个手动的
luke = Character("Luke Skywalker (Test)", "Human")
c3po = Character("C3PO (Test)", "Droid")
print(luke.info())
print(c3po.info())


#### Fetching Character data from swapi.co
BASE_URL = "https://swapi.dev/api/people" 

resp = requests.get(BASE_URL)
results_object = resp.json() 
people_list = results_object["results"]

characters = []
for p in people_list: #API中每个people的data，用Character class，append他们的info到characters = []里面；每个p用loop分别输入character_data这个参数里
    characters.append(Character(character_data=p))

for c in characters:
    print(c.info()) #再把每个打出来




'''
- A brief introduction to unit testing
        一个.py文件是一个module
        要创建multi-module program，选一个作为main.py然后拆开就行
        在mian.py里面 import自己定义的其他module
'''  



