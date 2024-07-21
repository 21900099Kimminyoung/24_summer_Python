# 첫째 줄에 테스트 케이스의 개수 T (1 ≤ T ≤ 100)가 주어진다. 
# 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 N은 짝수이고, 
# 2 < N ≤ 1,000,000을 만족한다.
# 500,001 까지 소수 인지 미리 계산한다
# 첫 수를 2로 잡은 경우 N-2 가 소수인지 확인 등등
import sys
import math
num = 1000001
prime = [False, False] + [True] * 999999
T = int(sys.stdin.readline().strip())

for i in range(2,num):
    if prime[i]:
        for j in range(i*2,num,i):
            prime[j] = False

for i in range(T):
    count = 0
    n = int(sys.stdin.readline().strip())
    for j in range(2,n//2+1):
        if prime[j] and prime[n-j]:
            count += 1
    print(count)



