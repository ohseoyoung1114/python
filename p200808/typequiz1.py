#quiz1

score = {'hong':{'math':95, 'eng':85, 'kor':90},
         'park':{'math':85, 'eng':100, 'kor':80},
         'kim':{'math':75, 'eng':65, 'kor':100}}

#[1.1] park의 모든 과목의 점수를 출력
#[1.2] kim의 kor점수만 출력
print('[1.1]:', score.get('hong'))
#print(score.get('kim'))
#print(type(score.get('kim')))
a1 = score.get('kim')
print('[1.2]:', a1.get('kor'))

#===================풀이================
#[1.1]
print('park:', score['park'])
#[1.2]
print('kim:', score['kim'].get('kor'))

#2
number = [100,200,100,500,200,600,300]

#number = set(number)
#number = list(number)
number = list(set(number))
number.sort()
print('[2.1]:', number)

number = set(number)
number.add(400)
#print(number)
number = list(number)
#print(number)
number.sort()
print('[2.2]:', number)


#3
jumin = '921103-1234567'
print('[3.1]:', jumin[0:2])
print('[3.2]:', jumin[2:4])
print('[3.3]:', jumin[4:6])
print('[3.4]:', jumin[7:8])
print('[3.5]:', jumin.replace("921103-", "920803-"))
