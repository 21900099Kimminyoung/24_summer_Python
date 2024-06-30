import sys
n = int(input())
score = list(map(int,sys.stdin.readline().split()))
M = max(score)
for i in range(n):
    score[i] = score[i]/M * 100
print(sum(score)/n)