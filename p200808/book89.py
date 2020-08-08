#p.89
a = {1:'hi'}

print(a[1])

a= {'a' : [1,2,3]}
print(a['a'][1])

#key 존재 여부에 다라 결과가 다르다.
#key 존재하지 않으면, 요소 추가

a[2] = (2,4,6)
print('a:', a)

#key존재하면, 요소의 값을 수정
a[2] = list(a[2])
print('a:',a)



#키 2의 값 리스트를 수정 : 인덱스 1의 요소값 3을 추가

a[2].insert(1, 3)
print('a:',a[2])

#p.92
a = {1: 'a', 1: 'b'}
print(a)

#p.93
a = {(1,2): 'hi'}
print(a)
