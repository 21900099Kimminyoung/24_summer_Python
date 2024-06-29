n = int(input())
num = int(n/4)
long = str()
for i in range(num):
    if i == 0:
        long = "long"
    else:
        long = long +" long"
print(long,"int")