
def list_remind(message, data):
    print('2', message, data[-1]) #2 please pick up bread
    message = 'don\'t forget!' #赋值新的message 不影响outer的reminder
    data.append('eggs') #append（）同一个data/groceries，所以groceries变了
    print('3', message, data[-1]) #3 don't forget! eggs

groceries = ['milk', 'bread']
reminder = 'please pick up'
print('1', reminder, groceries[-1]) #1 please pick up bread
list_remind(reminder, groceries) #调用函数 执行里面的两个print
print('4', reminder, groceries[-1]) ##！ 这里
