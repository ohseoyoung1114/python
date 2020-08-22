#한글처리를 위한 코딩
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#p.130
#
# treeHit = 0
#
# while treeHit < 10:
#     treeHit = treeHit + 1
#     print("나무를 %d번 찍었습니다." %treeHit)
#
#     if treeHit == 10:
#         print("나무 넘어갑니다.")



#p.132
#왼쪽에 변수가 선언되어있기때문에 여러줄의 문자열로 인식함
prompt = '''
1. Add
2. Del
3. List
4. Quit


Enter number : '''
number = 0
while number != 4:
    print("---------------------------------")
    print(prompt, end='')
    number = int(input())
    if number == 2:
        print("2.Del")
    elif number == 1:
        print("1.Add")
    elif number == 3:
        print("2.List")
    elif number == 4:
        print("4.Quit")
