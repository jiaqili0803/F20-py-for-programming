
def list_remind(message, data):
    print('2', message, data[-1]) #2 please pick up bread
    message = 'don\'t forget!'
    data.append('eggs')
    print('3', message, data[-1])

groceries = ['milk', 'bread']
reminder = 'please pick up'
print('1', reminder, groceries[-1]) #1 please pick up bread
list_remind(reminder, groceries) #调用函数
print('4', reminder, groceries[-1])
