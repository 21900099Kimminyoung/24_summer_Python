# 검색해아하는 단어의 집합 K, 검색당하는 단어의 집함 S
# S에서 K를 검색했을 때 몇개가 있는지 출력하라
import sys
N, M = map(int,sys.stdin.readline().split())
K = []
S = []
count = 0
for i in range(N):
    K.append(sys.stdin.readline().strip())
for i in range(M):
    S.append(sys.stdin.readline().strip())
for i in K:
    count = count + S.count(i)
print(count)