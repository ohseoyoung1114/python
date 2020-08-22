
#python에서 외부에서들어오는(input) 값은 보통 무낮열로 인식한다. 따라서 앞에 int, float등을 써줘서 설정해주거나 해야한다.
num = float(input('숫자 1개 입력 >>>'))
print('입력값: ', num)
print('자료형: ', type(num))


#정수2개를 입력받아서 덧셈결과 출력

# num1 = int(input('num1 >>>'))
# num2 = int(input('num2 >>>'))

####################################################

#여러개의 값 입력 받기

#[방법1]
#하나의 변수에 여러개의 값을입력받으면 튜플로 보여진다.
value = eval(input('정수두개 입력>>>'))
print('합', value[0] + value[1])

#[방법2]
n1, n2 = input('정수 2개 입력 >>>').split(',')
#split은 데이터를 구분할 수 있는 기준이 되는데 사용자가 설정가능함

print('첫번재 입력값: ', n1)
print('두번재 입력값: ', n2)

n1 = int(n1)
n2 = int(n2)

print('자료형 :', type(n1))
