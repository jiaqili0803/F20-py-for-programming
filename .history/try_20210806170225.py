
def dict_update(local_dict):
    local_dict['g'] = 'grapefruit'
    local_dict['n'] = 'nectarine'
global_dict = {'g': 'grape', 'p': 'plum', 'o': 'orange'}
dict_update(global_dict)
print(global_dict['g'])
print(global_dict['n'])
print(global_dict['p'])

