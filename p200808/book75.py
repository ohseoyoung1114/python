#p.75
a = [1, 2, ['a','b', ['Life', 'is']]]

print(len(a))
print(a[2][2][0][2])

#p.78
a = [1,2,3]
print(str(a[2]) +'hi')

#요소값 1개를 인덱스로 접근하여 변경
a[2] = 4
print('a:', a)

#요소값 2를 del 함수를 이용하여 삭제
del a[1]
print('a:', a)

del a[0:]
print('a:', a)

#p.82

a = [1,2,3,1,2,3]

a.remove(3)  #리스트에서 첫번째 나오는 X를 삭제하는 함수
print(a)


#p.83
a = ['one', 'two', 'three']
print(a.pop(1))  #리스트의 맨마지막 요소를 돌려주고 그 요소는 삭제한다.
print(a)
a.remove
