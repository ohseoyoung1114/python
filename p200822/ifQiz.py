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


#[5] 선생님 해답
num = int(input('정수 1개 입력 >>> '))

if num5 < 0 :
    print('0미만의 수')

elif num5 < 10 :
    print('0이상 10미만의 수')

elif num5 < 20 :
    print('10이상 20미만의 수')

elif num5 < 30 :
    print('10이상 20미만의 수')

else:
    print('30이상의 수')
