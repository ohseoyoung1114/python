

num = 0

formatNum = 'num data %+4d.'%num
print(formatNum)

n1 = 10         #10진수
n2 = 0o10      #8진수
n3 = 0x10      #16진수

print('n1: %d, n2: %d, n3: %d'%(n1,n2,n3))
print('n1: %d, n2: %o, n3: %x'%(n1,n2,n3))
print('n1: %d, n2: %#o, n3: %#x'%(n1,n2,n3))


fo = 2.34
print('fo: %f'%fo)
print('fo: %.2f'%fo)     #소수 둘쨋자리까지 프린트
print('%.2f'%fo)
print('%6.2f'%fo)        #전체를 6자리로 표현 소수 둘쨋자리까지 보여지고 오른쪽 정렬
print('%3.2f'%fo)        #데이터는 4자린데 전체를 3자리로 표현하면 그래도 4자리로 보여짐
                                #지정된 자리보다 데이터가 더크면 데이터가 다 보여짐
                                #전체자리는 강제성은 없다. 소숫점은 강제성이 있다.



#c1 = 'A'
#c2 = 'a'
c1, c2 = 65, 97
print("c1: %c, c2: %c"%(c1, c2))
print("c1: %d, c2: %d"%(c1, c2))
print("c1: %s, c2: %s"%(c1, c2))

print('실수데이터 : %s'%fo)

print('성공률 %d%입니다.'%100)




































