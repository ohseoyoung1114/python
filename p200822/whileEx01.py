#반복문
num = 0

while num<3:               #조건
    print('num : %d' %num)   #1
    num +=1                  #증감식

print("success!!")

num=0
while True:               #조건
    print('num : %d' %num)   #1
    num +=1
    if num == 3:
        break

print("success!!")


num = 0
while num < 10:
    num+= 1
    if num % 3 ==0:
        break
    print('num:')


#
# print('num :', num)   #2
# num +=1
#
# print('num :', num)   #3
# num +=1
