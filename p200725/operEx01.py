

#대입연산자
#[형태]
#변수 = 값

n1 = 6
n2 = 7

result = n1 ** 2
print('제곱 :', result)


result = n2 / 3
print('몫1 :', result)

result = n2 // 3
print('몫2 :', result)

#나머지 연산자 : %
# - 짝수/홀수를 찾을때
# - 짝수/홀수 구분할 떄
# - ~배수를 찾을때

result = n2 % 3
print('나머지 :', result)



print('연산전>>> n1 :', n1, 'n2 :', n2)

n1 = n1+ n2
print('n1 :', n1)
print('연산전>>> n1 :', n1, 'n2 :', n2)



#1증가
n1 = n1 + 1
print('1증가된 n1 :', n1)


#[논리연산자]
print('현재값 >>> n1 :', n1, 'n2 :', n2)
print('and연산자 :', n1 > 10 and n2 > 10)
print('or연산자 :', n1 > 10 or n2 > 10)
print('not연산자 1):', not n1 > 10)
print('not연산자 2):', not True)
print('not연산자 3):', not 100)
print('not연산자 4):', not 0)
print('not연산자 5):', not 'Hi') #여기서의 true는 " "안에 문자열이 있냐 없냐 그래서 문자가 있기떄문에 true
print('not연산자 6):', not '')


#[조건연산자]
#true일때 if 조건식 else false 일때
n1 = 5
print('10보다 크다' if n1>10 else '10보다 작거나 같다.')


#[문제1]
n1 = 10
n2 = 15
n1, n2 = 10, 15
result =0
'''
if n1 > n2 :
    result = n1
else :
    result = n2
'''
result = n1 if n1>n2 else n2
print('result :', result) 

#[문제2]
'''
if n1 > 0 :
    value = '양수'
else :
    value = '0 또는 음수'
'''
value = '양수' if n1>0 else '0또는 음수'

print('value :', value)

    






























































































