# 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. 
# n == 1 이면 다음으로 넘어가기
# 1 ≤ n ≤ 123,456
# 미리 계산해두기 그럼 한번만 소수인지 확인하면 된다. => 소수이면 1 아니면 0
import sys
import math

num = 123456*2 + 1
n_prime = [1]*num

def is_prime(x):
    if x == 1 or x == 0:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

for i in range(num):
    if not is_prime(i):
        n_prime[i] = 0

while True:
    count = 0
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break
    for i in range(n+1,2*n+1):
        count += n_prime[i]
    print(count)
