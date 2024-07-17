# math lcm함수를 이용해서 최소 공배수를 구한다.
# import sys
# import math
# n, m = map(int,sys.stdin.readline().split())
# print(math.lcm(n,m))

#최대 공약수를 구하고 두수의 곲 // 최대공약수 => 최소공배수 이다.
import sys
import math
n, m = map(int,sys.stdin.readline().split())
if n > m:
    n, m = m, n
for i in range(n,0,-1):
    if n%i ==0 and m%i == 0:
        gcd = i
        break
print((n*m)//gcd)
