# M N을 입력받아서 두수 사이의 소수를 구해서 출력
import sys
import math
M, N = map(int,sys.stdin.readline().split())
check = 0
for i in range(M, N + 1):
    if i == 1:
        continue
    for j in range(2,int(math.sqrt(i))+1):
        if i % j == 0:
            check = 1
            break
    if check == 0:
        print(i)
    else:
        check = 0