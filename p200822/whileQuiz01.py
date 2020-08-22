#사용자에게 연속해서5개의 정수를 입력받아 다음과 같이 출려되도록 하시오
# 입력이 몇번째인지 출력
#입력된 값의 합

idx = 1
value = []  #입력된 값을 리스트에 저장하기위한변수
count = 0   #누적합이 보관될 변수
while idx < 6:
    #num = int(input('%d번째' %idx))
    num = int(input('{}번째 입력 : '.format(idx)))
    count = count + num
    value.append(num)
    idx = idx + 1

print('누적합 : ' , count)
print('입력된값 : ', value)
