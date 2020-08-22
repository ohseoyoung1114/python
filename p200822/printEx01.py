#print 함수
help(print)

note = open('D:\\pyhton\\project\\p200822\\test.txt', 'w')
#note = open('D:\pyhton\project\p200822\test.txt', 'w')
# \n 엔터 , \t 탭 으로 인식하기 때문에 위 코드 에러

print('value1', 'value2', sep='-', end='/')

#생성되는 파일에 출력해보기!
print('data1', 'data2', file=note)  #출력대상이 파일이 모니터(표준출력장치)가 아니라 파일이 된다. / 파일에 기록되는 함수는 따로 있음
print('success')

note.close()

#한글처리를 위한 코딩
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#[quiz]
#출력형태 : 연락처는 010-1111-1111입니다.
print('연|락처는', end=' ')
print('010', '1111', '1111', sep='-', end='')
print('입니다.')
