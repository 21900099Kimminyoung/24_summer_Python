import sys
n = int(input())
num = list()
for i in range(n):
    a, b = map(int,sys.stdin.readline().split())
    new = [a,b]
    num.append(new)
for i in range(n):
    print("Case #"+str(i+1)+":",num[i][0],"+",num[i][1],"=",num[i][0]+num[i][1])