import sys
n = int(input())
sum = list()
for i in range(n):
    a, b = map(int,sys.stdin.readline().split())
    sum.append(a+b)
for i in range(n):
    print("Case #"+str(i+1)+":",sum[i])