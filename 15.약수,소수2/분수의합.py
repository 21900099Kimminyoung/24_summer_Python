# 두 분수를 입력받는다.
# 분모끼리 분자끼리 곱한다.
# 두 수의 약수를 구해 두수를 나누어 준다.
import sys
import math
def gcd(A,B):
    while A%B != 0:
        r1 = A%B
        A = B
        B = r1
    return B

A1, B1 = map(int,sys.stdin.readline().split())
A2, B2 = map(int, sys.stdin.readline().split())
A = A1 * B2 + A2 * B1
B = B1 * B2
Gcd = gcd(A,B)
print(A//Gcd,B//Gcd)