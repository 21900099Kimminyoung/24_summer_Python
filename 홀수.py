n = []
for i in range(7):
    num = int(input())
    if(num % 2 != 0):
        n.append(num)
if not n:
    print(-1)
else:
    print(sum(n))
    print(min(n))