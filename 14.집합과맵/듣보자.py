# 듣어보지 않은사람 n명 보지도 못한 사람 m명 중에서 듣도 보도 못한 사람을 골라라
import sys
N, M = map(int,sys.stdin.readline().split())
D = {}
count = 0
for i in range(N):
    D[sys.stdin.readline().strip()] = False
for i in range(M):
    name = sys.stdin.readline().strip()
    if name in D:
        D[name] = True
        count += 1
print(count)
D = dict(sorted(D.items()))
for i in D:
    if D[i] == True:
        print(i)