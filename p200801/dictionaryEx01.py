#딕셔너리
# : 하나의 데이터가 키:값쌍으로 이루어짐
# : 저장순서를 유지하지 않음 -> 인덱스 사용할 수 없음
# : 키를 통해 값에 접근
# : 여러 개의 데이터(요소)를 {}로 묶어서 관리
# dc = {key:value}
dc = {'name': 'hong', 'addr': 'Seoul Gangnam', 'phone': '010-1111-1111'}
print(len(dc))  #요소의 갯수
print(dc['name'])   #키를 통해서 값을 찾아온다. 키는 중복해서 X 값은 중복 O/ 딕셔너리는 인덱스를 사용하지 않는다.
dc['name'] = 'Kim'  #이미 존재하는 키면 값 변경
print(dc)
print(type(dc))

dc['age'] = 24      #존재하지 않는 키면 값 추가
print(dc)

del dc['addr']
print(dc)

#키만 추출
print('key :', dc.keys())
#값만 추출
print('value :', dc.values())

#get함수를 이용한 값 추출
#print('age :', dc.get('addr', 'nokey'))
#print('age :', dc['addr'])

#in연산자 : 데이터의 존재여부
print('age' in dc)
print('addr' in dc)
print(dc)
print('Kim' in dc.values())

#딕셔너리의 요소를 모두 삭제
dc.clear()
print(dc)
