import sys
N = int(input())
result = [0]*10000
for i in range(N):
    n = int(sys.stdin.readline().strip())
    result[n-1] += 1
for i in range(10000):
    for j in range(result[i]):
        print(i+1)