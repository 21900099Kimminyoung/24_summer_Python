import sys
num = list()
while True:
    try:
        a,b = map(int,sys.stdin.readline().split())
        num.append(a+b)
    except:
        break
for i in range(len(num)):
    print(num[i])
