n = int(input())
star = 1
for i in range(n):
    for j in range(star):
        print("*",end="")
    star = star + 1
    print("")