#81개의 숫자를 입력받아서 저장한다
#최대값과 그 인덱스를 저장한다.
import sys
n = []
max = 0; N = 0; M = 0
for i in range(9):
    n.append(list(map(int, sys.stdin.readline().split())))
for i in range(0,9):
    for j in range(0,9):
        if(n[i][j] >= max):
            max = n[i][j]
            N = i + 1
            M = j + 1
print(max)
print(N,M)