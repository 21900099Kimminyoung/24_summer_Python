import sys
N = int(sys.stdin.readline().strip())
p_inf = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
s_inf = list(map(int,sys.stdin.readline().split()))
result = {}
for i in p_inf:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
for i in s_inf:
    if i in result:
        print(result[i],end=' ')
    else:
        print(0,end=' ')
