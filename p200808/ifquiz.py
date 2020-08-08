#[2]사용자에게 정수 1개를 입력받아서 양수/음수/0 구분하여 출력

num = int(input('[2]정수 1개 입력:'))

if num>0:
    print('양수')

elif num == 0 :
    print('0')

else:
    print('음수')


num2 = int(input('[3]정수 1개 입력:'))

if num2 % 2 == 0 :
    print('짝수')

else:
    print('홀수')

#[4]사용자에게 정수 2개를 입력받아서, 큰 값 출력
num3, num4 = eval(input('[4]정수 2개 입력:'))

if num3 > num4 :
    print(num3)

elif num3 == num4 :
    print('same')

else:
    print(num4)


#[5]사용자에게 정수 1개를 입력 받아서, 해당되는 값의 범위를 출력
num5 = eval(input('[5]정수 1개 입력:'))

if num5 < 0 :
    print('0미만의 수')

elif 0 <= num5 < 10 :
    print('0이상 10미만의 수')

elif 10 <= num5 < 20 :
    print('10이상 20미만의 수')

elif 20 <= num5 < 30 :
    print('10이상 20미만의 수')

else:
    print('30이상의 수')
