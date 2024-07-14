n = int(input())
num = map(int,input().split())
num = list(num)
obj_num = int(input())
match_num = 0
for i in range(len(num)):
    if(obj_num == num[i]):
        match_num = match_num + 1
print(match_num)