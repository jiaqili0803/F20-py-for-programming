lstA = [106]

lstB = lstA #注意这句赋值的位置 B一直会等于原来的A

print(lstA)   #[106] [106]
print(lstB)

lstA.append(206) #相当于改变原A,所以AB都变[106, 206],[106, 206]

print(lstA) 
print(lstB)

lstA = lstA[1:] #slice相当于创建了一个新A，但是B还是等于原来的A

print(lstA)
print(lstB)

lstA.append(506)
print(lstA)
print(lstB)
#print(lstB)



