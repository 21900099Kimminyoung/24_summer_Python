n = int(input())
sum = list()
for i in range(n):
    a, b = map(int,input().split())
    sum.append(a+b)
for i in range(n):
    print(sum[i])