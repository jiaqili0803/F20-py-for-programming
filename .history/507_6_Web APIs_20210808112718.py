'''

- What is the Web? 
    - GET request是最常见的网页浏览请求（URL），也可以发送数据到server，using a technique called “query strings.”
    
    URL组成部分：
        - Protocol协议: HTTPS、ftp、mailto...
        - Subdomain and Domain name: 如si.umich.edu 和 wolverineaccess.umich.edu 
        - Port: 接入端口 0-65535，有特定规则；url一般省略 使用默认(port 80 for HTTP and port 443 for HTTPS)
        - Path: to the name of specific resource (e.g., file) ；https://www.si.umich.edu/content/msi, the path “content/msi” 
        - Query and Parameters: url中？后的parameter（query string），用来更准确的传达我们要request什么；格式：param_name_1=param_value_1&param_name_2=param_value_2&...
        - Fragment: in-page “anchors” 自动定位到页面某一位置
        
    main parts of the URL：
        - The endpoint: ？之前的everything 
        - The query string:  ？之后的parameters

    
- What are Web APIs and how do we access them? 
    - APIs in general
        Application Programming Interface
        
    - Web APIs in particular
        比一般的API方便：不需要安装更新，支持不同语言，不同平台
        也有劣势：可能会慢，用的人太多质量下降
        现在有22000个WEB API：https://www.programmableweb.com/apis/directory
 
     - Accessing Web APIs via the browser
        根据API说明
        用endpoint？query string修改url
        得到JSON数据
    
    
- Access the Web and Web APIs in Python
    - Requests库,比urlib好用，是python API,可以获取任何类型web data
        导入 import requests
        方法 requests.get('URL') 
        attibutes们：.text, .status_code, ... 
        常见status：200 (OK), 404 (Not Found), and 403 (Forbidden)
        可以建立parameter_dict，避免一次太长的url
        '''
#得到内容
import requests
response = requests.get("http://datamuse.com") #得到object
print(response.text) #text attribute

#得到状态            
import requests
response = requests.get("http://datamuse.com")
print(response.status_code) # prints 200, or "OK"
response = requests.get("http://datamuse.com/nothinghere")
print(response.status_code) # prints 404, or "Not Found"

#建立parameter_dict
baseurl = "https://api.datamuse.com/words" #base,endpoint
params_dict = {'rel_rhy':'blue'} #字典组成 相当于 key=values在？后面
response = requests.get(baseurl, params_dict) #params_dict带进来
 ## actually send the request: https://api.datamuse.com/words?rel_rhy=blue

status_code = response.status_code # 200 means "OK"
response_body = response.text # this is typically what you want
print(response_body)
    
''' 

- What is JSON? 
    - ！Strings！ that represent data structures（虽然和py dict/list结构一样，但还是string）
    - import json
    - json.loads(方法  json str 变 py dict/list
    - 反之， json.dumps()   
'''
#json.loads(）；json str 变 py dict/list
import json #用来解析json格式string
json_str = '''
    [{"a":"apple", "b": "banana"},{"a":"apricot", "b":"blueberry"}]
    '''
fruit_dict_list = json.loads(json_str) #json.loads(）使变成py dict/list

print(type(json_str))           # prints <class 'str'>
print(type(fruit_dict_list))    # prints <class 'list'>
print(type(fruit_dict_list[0])) # prints <class 'dict'>
print(fruit_dict_list[0]["b"])  # prints banana

#json.dumps()  
import json
the_dict = {'g': 'grape', 'p': 'plum', 'n': 'nectarine'}
dict_json_str = json.dumps(the_dict)
print(type(dict_json_str)) #<class 'str'> 成功变为json
print(dict_json_str)



'''
    - 优点：Standard notation—cross language, cross platform, highly portable


- How do we work with JSON in Python?
    - the json library, `json.loads()`, `json.dumps()`

'''