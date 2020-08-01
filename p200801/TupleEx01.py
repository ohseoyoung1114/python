# 튜플(tuple)
# 튜플안에 있는 값은 변경할 수 없다. 그냥 써야함

lt = [1, 2, 3]
tu = (1, 3, 5, 3.4, [8, 9], (7, 4), 'hello')

tu = list(tu)  #튜플을 리스트로 변경함 -> 이제 요소값을 수정할 수 있다.

print(tu[1])
print(type(tu[1]))
print(type(tu[4]))

print('tu: ', tu)
print('type(tu): ', type(tu))

tu1 = ()  #빈튜플
print('tu1: ', tu1)
print('type(tu1): ', type(tu1))

tu2 = (10)   #요소가 1개인 튜플을 사용하고 싶을 때는 (10,)이렇게 써줘야함
print('tu2: ', tu2)
print('type(tu2): ', type(tu2))

tu3 = 10, 20   #요소가 2개인 튜플, 한개의 변수에 괄호없이 요소가 여러개면 튜플로 인식
print('tu3: ', tu3)
print('type(tu3): ', type(tu3))
