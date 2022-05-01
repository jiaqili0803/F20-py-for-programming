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
    - Requests, `requests.get()`, `response` objects
    - parameters and query string
    
    
- What is JSON? 
    - Strings that represent data structures
    - Standard notation—cross language, cross platform, highly portable


- How do we work with JSON in Python?
    - the json library, `json.loads()`, `json.dumps()`

'''