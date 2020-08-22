#[1]구구단 2단을 출력
num = 1
while num<10:
    total = 2*num
    #print(total)
    print("2 * %d = %d" % (num, num*2))
    num = num + 1


#[2] 1~10 까지 더한 값을 출력
count = 0
num1 = 1
while num1 <= 10:
    count = count + num1
    num1 = num1 + 1

print("success")
print(count)
