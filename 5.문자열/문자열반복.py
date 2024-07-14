import sys

n = int(input())
lists = []
for i in range(n):
    R, S = sys.stdin.readline().split()
    R = int(R)
    answer = ''
    for char in S:
        answer += char * R
    lists.append(answer)
print(*lists,sep='\n')