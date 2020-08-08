# 리스트: [요소1, 요소2]
# 튜플 : (요소1, 요소2)
# 딕셔너리: {키1:값1, 키2:값2} --> 저장순서를 보장하지 않는다.
# 집합 : {요소1, 요소2} --> 저장순서를 보장하지 않는다., 중복제거, 순서가 보장되지 않기때문에 인덱스를 사용할 수 없음

s1 = {2, 4, 6, 4, 8, 4}

print('s1 :', s1) #알아서 중복제거
print('type :', type(s1))

lt = [1, 3, 5, 3, 7]
print('lt: ', lt)
lt = set(lt)
print('lt->set :', lt) #알아서 중복제거
print('type :', type(lt))


# s2 = {'Hello'}  --> 데이터로 요소 하나를 넣은 것
s2 = set('Hello')  # --> 데이터 하나를 각각의 요소 인식
print('s2 :', s2)
print('type :', type(s2))

s3 = {1,2,4,5,7}
s3.add(8)   # add는 한개의 값만 추가가된다.
s3.update([9,10])  #update는 리스트로 여러개의 값을 추가할 수 있다.
s3.remove(8)
print('s3: ', s3)

#집합 s1과 s3의 교집합
#방법1) 연산자
print(s1 & s3)
#방법2) 함수
print(s1.intersection(s3))  # s1을 기준으로 s3와 같은 데이터를 찾는다.


#집합 s1과 s3의 합집합
#방법1) 연산자
print(s1 | s3)
#방법2) 함수
print(s1.union(s3))  # s1을 기준으로 s3의 데이터와 합친다.


#집합 s1과 s3의 차집합
#방법1) 연산자
print(s1 - s3)

#방법2) 함수
print(s1.difference(s3))  # s1을 기준으로 s3의 데이터를 뺀다.
