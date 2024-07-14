import sys
a, b = 1, 1
n = 0
num = list()
while True:
    a, b = map(int,sys.stdin.readline().split())
    if(a==0 and b==0):
        break
    list = [a ,b]
    num.append(list)
    n = n + 1
for i in range(n):
    print(num[i][0]+num[i][1])

    