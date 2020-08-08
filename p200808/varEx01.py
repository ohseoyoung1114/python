from copy import copy

data = [2,4,6]
#copyData = data[:]
copyData = copy(data)

#id는 address를 찾는다.
print(data)
print(id(data))
print(id(copyData))

data[0] = 10
print(data)
print(copyData)

num1 = 10
num2 = 10
print(id(num1))
print(id(num2))
