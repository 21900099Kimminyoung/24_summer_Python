import sys
n = int(input())
string = [sys.stdin.readline().strip() for i in range(n)]
for i in range(n):
    print(string[i][0]+string[i][len(string[i])-1])