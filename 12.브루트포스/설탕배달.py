n = int(input())
result = []
k = n//5 + 1
for i in range(k):
    sum = (i)
    m = n - (i * 5)
    if m % 3 == 0:
        sum = sum + m//3
        result.append(sum)
if not result:
    print(-1)
else:
    print(min(result))
