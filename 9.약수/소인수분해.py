# n 을 입력받는다.
# 입력받은 n을 나누었을 때 1이 나올때 까지 반복한다.
import sys
n = int(sys.stdin.readline().strip())
i = 2
while i < n:
    if n % i == 0:
        print(i)
        n //= i
    else:
        if i == 2:
            i += 1
        else:
            i += 2
if n > 1:
    print(n)