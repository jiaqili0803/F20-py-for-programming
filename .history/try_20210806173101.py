
def list_remind(message, data):
    print('2', message, data[-1])
    message = 'don\'t forget!'
    data.append('eggs')
    print('3', message, data[-1])

groceries = ['milk', 'bread']
reminder = 'please pick up'
print('1', reminder, groceries[-1])
list_remind(reminder, groceries)
print('4', reminder, groceries[-1])
