import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


# 'hi'요소를 찾아서 'hello'로 변경

data = ['hi', 100, 200, 'good', 300]

# print(data.index('hi'))
# data.remove('hi')
# a = data.pop(data.index('hi'))
# data.insert(2, 'hello')
a = data.index('hi')
data[a] ='hello'
print(data)
