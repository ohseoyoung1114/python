#변수에 값 설정하는 여러 형태
#[방법1]

a = 'python'
b = 'life'

print('a: {}, b: {}'.format(a,b))

#[방법2]
a,b = 'python', 'life'
print('a: {}, b: {}'.format(a,b))

#[방법3]
a=b='ptyhon'
print('a: {}, b: {}'.format(a,b))

#2개 변수의 값을 서로 교환
one=100
two=200
one, two = two, one
print('one: {}, two: {}'.format(one,two))
