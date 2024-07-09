import sys
n = int(input())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))
l.sort()
print(*l,sep='\n')