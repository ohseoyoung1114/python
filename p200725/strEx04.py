'''
[문자열포맷팅]
'''

apple  = 5
banana = 6

print('사과 :', apple, '개, 바나나 :', banana, '개')

print('사과 : %d, 바나나 : %d' %(apple, banana))

print('%d'%apple)
print('%6d'%apple) #6자리, 오른쪽 정렬로 출력
print('%-6d'%apple) #6자리, 왼쪽 정렬로 출력
print('%+6d'%apple)
print('%06d'%apple) #빈공간이 있으면 0으로 채워라

#서식문자: %ㅊ
c1 = 65 #A가 갖는 아스키코드 값
c2 = 97 #a가 갖는 아스키코드 값

print('%c, %c'%(c1,c2))
print('%d, %d'%(c1,c2)) #이게 되는 이유는? 아스키코드를 받을 수 있기때문 65 번에 해당하는 문자를 받아옴

