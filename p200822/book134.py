#p.134
#한글처리를 위한 코딩
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

coffee = 3
money = 300

while True:      #무한반복문
    money = int(input('돈을넣어주세요:'))

    if money == 300:
        print('커피를 줍니다.')
        coffee = coffee - 1
        print("남은 커피의 양은 %d개 입니다." %coffee)
        print('\n')

    elif money>300:
        print('거스름돈 %d를 주고 커피를 줍니다.' %(money-300))
        coffee = coffee - 1
        print('\n')

    else:
        print("커피를 주지않습니다.")
        print('남은 커피의 양은 %d개 입니다.'%coffee)
        print('\n')

    if coffee == 0:
        print("커피가 다 나갔습니다.판매중지")
        break
