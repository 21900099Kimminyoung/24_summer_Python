# https://wikidocs.net/16043
import sys
n = int(sys.stdin.readline().strip())
X = list(map(int,sys.stdin.readline().split()))
X1 = sorted(X)
X1 = dict.fromkeys(X1)
con = 0
for i in X1:
    X1[i] = con
    con+=1
for i in range(n):
    X[i] = X1[X[i]] # key 로 접근 하는 것
print(*X)