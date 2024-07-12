import sys
n = int(input())
num = []
for i in range(n):
    k = int(sys.stdin.readline().strip())
    num.append(k)
result = dict.fromkeys(num)
result = list(map(int,result))
result.sort()
print(*result,sep='\n')