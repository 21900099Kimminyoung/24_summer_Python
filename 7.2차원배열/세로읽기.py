#다섯줄을 입력받아서 세로로 읽는 것을 출력
#만약 공백이면 무시하고 다음거 출력
# 0 0 0
# 1 0 0
# 2 0 0
# 0 0 1
# 1 0 1
# 2 0 1
# 
import sys
S = []
max = 0
for i in range(5):
    S.append(sys.stdin.readline().split())

for i in range(5):
    if(max < len(S[i][0])):
        max = len(S[i][0])

for i in range(max):
    for j in range(5):
        if len(S[j][0]) > i:
            print(S[j][0][i],end='')
print()