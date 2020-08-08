
num = 100

print('num :', num)

#입력함수
#정수2개를 입력받은 후, 더한 값을 출력
#num1 = int(input('입력1 :'))
#num2 = int(input('입력2 :'))

#정수, 실수에 맞춰서 변환해주는게 eval함수임
#num1, num2 = eval(input('입력1 :')), eval(input('입력2 :'))
num1, num2 = eval(input('2개 입력 :'))

print(type(num1))
print(type(num2))

print('합:', num1 + num2)

print('실행완료')
