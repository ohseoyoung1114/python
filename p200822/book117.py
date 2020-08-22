#p.117
#한글처리를 위한 코딩
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

money = True

if  money:
    print("택시")

else:
    print('걸어라')


#p.123

money = 2000
card = True
if money >= 3000 or card:
    print('taxi')

else:
    print('on foot')

#p.124
#in 뒤에는 여러개의 값이 와야한다.
#in 뒤의 값에 앞에 선언한 값이 잇는지 확인

print( 'apple' not in ['apple', 'banana'] )

pocket = ['paper', 'cellphone', 'money']
card = True
if 'money' in pocket:
    print('taxi')
else:
    if card:
        print('카드가 있다면 taxi')
    else:
        print('카드가 없으니 걸어라')
    print('on foot')


#p.128 조건연산자
