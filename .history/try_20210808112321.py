import json

the_dict = {'g': 'grape', 'p': 'plum', 'n': 'nectarine'}
dict_json_str = json.dumps(the_dict)
print(type(dict_json_str)) #<class 'str'> 成功变为json
print(dict_json_str)



