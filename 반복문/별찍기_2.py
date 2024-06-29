n = int(input())
star = 1
blank = n-1
for i in range(n):
    for j in range(blank):
        print(" ",end="")
    for j in range(star):
        print("*",end="")
    blank = blank - 1
    star = star + 1
    print("")