lstA = [106]

lstB = lstA

print(lstA)   #[106] [106]
print(lstB)

lstA.append(206)

print(lstA)
print(lstB)

lstA = lstA[1:]

print(lstA)
print(lstB)

lstA.append(506)
print(lstA)
print(lstB)
#print(lstB)



