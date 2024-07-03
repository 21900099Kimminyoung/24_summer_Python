import sys
N, M = list(map(int, input().split()))
A = []; B = []
for i in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))
for i in range(N):
    B.append(list(map(int, sys.stdin.readline().split())))
for i in range(N):
    for j in range(M):
        A[i][j] = A[i][j] + B[i][j]
for i in A:
    for j in i:
        print(j,end=' ')
    print()
