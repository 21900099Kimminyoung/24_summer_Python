import sys
n = int(input())
c = []
sum = n*100
for i in range(n):
    c.append(list(map(int,sys.stdin.readline().split())))
for i in range(1,n):
    if c[i][0] >= c[i-1][0]:
        r = abs(c[i-1][0] + 10 - c[i][0])
        if c[i][1] <= c[i-1][1]:
            co = abs(c[i-1][1] + 10 - c[i][1])
            sum = sum - (r * co)
        elif c[i][1] > c[i-1][1]:
            co = abs(c[i][1] + 10 - c[i-1][1])
            sum = sum - (r * co)
    elif c[i][0] < c[i-1][0]:
        r = abs(c[i][0] + 10 - c[i-1][0])
        if c[i][1] <= c[i-1][1]:
            co = abs(c[i-1][1] + 10 - c[i][1])
            sum = sum - (r * co)
        elif c[i][1] > c[i-1][1]:
            co = abs(c[i][1] + 10 - c[i-1][1])
            sum = sum - (r * co)
print(sum)