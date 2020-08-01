


st = '  Hello  '

#문자수
print('문자 수 :', len(st))
print('문자l의수 :', st.count('l'))
print('문자l의수 :', 'Hello'.count('l'))
print('|' + st + '|')
print('|' + st.lstrip() + '|') #왼쪽 공백 없앰
print('|' + st.rstrip() + '|') #오른쪽 공백 없앰
print('|' + st.strip() + '|') #양쪽 공백 없앰
#print('|' + st.replace("  ", "") +'|')

print(st.upper()) #대문자로 변경
print(st.find('a')) #e의 index를 찾아줌 #없는 문자를 찾으면 -1 반환
'''
print(st.index('a')) #e의 index를 찾아줌 #없은 문자를 찾으면 에러
'''
print(st.replace('ello', 'i'))

quiz = 'TIme is too fast.'
startIdx = quiz.index('too')
endIdx = startIdx + len('too')
print(startIdx)
print(quiz[startIdx:endIdx])
print(quiz[quiz.index('too'):quiz.index('too') + len('too')])

