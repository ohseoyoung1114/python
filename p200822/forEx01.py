#for문
#for 변수 in 여러값:

odd = [1,3,5]
for o in odd:
    print(o)

#range 함수에서 (0,0,0) 세번째 값은 증가하는 값을 설정할 수 있다.
#설정하지 않으면 1이 디폴트
#range(끝값)#range(시작값, 끝값)#range(시작값, 끝값, 증감값)

number = range(1, 11, 2)
for r in number:
    print(r, end=' ')
print('\n' + '-' * 20)

for b in range(10,0,-1):
    print(b, end=' ')
print('\n' + '-' * 20)

a = [(1,2), (3,4), (5,6)]
for first, last in a:
    print(first+last)
print('\n' + '-' * 20)

data = range(0,2)
for data in a:
    #print(sum(data))
    #print(data[0] + data[1])
