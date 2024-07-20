import sys
import math
n = int(sys.stdin.readline().strip())

def is_prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

for i in range(n):
    l = int(sys.stdin.readline().strip())
    while True:
        if is_prime(l):
            print(l)
            break
        else:
            l = l + 1
        



