#영어로 입력을 받는다
#영어를 숫자로 변환 : ABC = 1, DEF = 2 ...
#누르고 싶은 번호까지 돌리는데 필요한 시간 구하기 . 1은 2초 걸리고 나머지는 1초씩 추가
import sys
S = sys.stdin.readline().strip()
num = [0] * len(S)
time = 0
for i in range(len(S)):
    if(S[i] < 'D'):
        num[i] = 2
    elif(S[i] < 'G'):
        num[i] = 3
    elif(S[i] < 'J'):
        num[i] = 4
    elif(S[i] < 'M'):
        num[i] = 5
    elif(S[i] < 'P'):
        num[i] = 6
    elif(S[i] < 'T'):
        num[i] = 7
    elif(S[i] < 'W'):
        num[i] = 8
    else:
        num[i] = 9
for i in range(len(num)):
    time = time + 1 + num[i]
print(time)