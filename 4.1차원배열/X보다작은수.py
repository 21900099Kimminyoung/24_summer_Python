n, x = map(int,input().split())
list = list(map(int,input().split()))
small_num = []
for i in range(n):
    if(x > list[i]):
        small_num.append(list[i])
print(*small_num,sep=" ")
