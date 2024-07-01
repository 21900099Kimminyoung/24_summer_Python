#문장을 입력받고 단어의 수를 구하기
#단어와 단어 사이에는 공백하나, 마지막에 공백이 하나 추가될 수도 있다.
import sys
S = sys.stdin.readline().strip()
pre = ' '
count = 0
for char in S:
    if(pre == ' ' and char != ' '):
        count = count + 1
    pre = char
print(count)