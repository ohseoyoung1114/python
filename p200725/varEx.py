

'''
200725 수업 시작

'''

'''

[자료형] : 데이터의 종류
- 정수 : int
- 실수 : float
- 문자열 : str
- 논리 : bool

'''
'''
<변수명>
- 문자로 시작
- 숫자로 시작X
- 변수명 사이에 띄어쓰기 사용X
- '_'는 사용 가능

'''


#변수선언
#변수선언에서 자료형을 쓰지 않기때문에 편리함
#파이썬은 정수가 int하나임 (다른언어에서는 int, char, short 등등 여러개)
#파이썬은 실수 됨

num = 5
print('num: ', num)
print('자료형: ', type(num))

num = 2.3
print('num: ', num)
print('자료형: ', type(num))

num = 'hi'
print('num: ', num)
print('자료형: ', type(num))

num = True
print('num: ', num)
print('자료형: ', type(num))


#[bool함수]
print('10의 논리값 :', bool(10))
print('-10의 논리값 :', bool(-10))
print('0의 논리값 :', bool(0))

print('hi의 논리값 :', bool('hi'))
print('빈 문자열의 논리값 :', bool(''))

str1 ='20'
num = 20
print('str1의 자료형', type(str1))
print('덧셈 :', str1 + str(num))

str1 = int(str1)
print('str1의 자료형 :', type(str1))
print('덧셈 :', str1 + num)

print('실수데이터 :', float(str1))
























































