a = [1,2,3]
b=a
a = a[1:]

print(a)
print(b)


lstA = [106]

lstB = lstA

print(lstA)   #[106] [106]
print(lstB)

lstA.append(206) #相当于改变原A,所以AB都变[106, 206],[106, 206]

print(lstA) 
print(lstB)

lstA = lstA[1:]

print(lstA)
print(lstB)

lstA.append(506)
print(lstA)
print(lstB)
#print(lstB)



