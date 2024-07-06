# n 을 입력받는다.
# 입력받은 n을 나누었을 때 1이 나올때 까지 반복한다.
n = int(input())
i = 2
while True:
    if(n%i == 0):
        print(i)
        if n/i == 1:
            break
        n = n/i
        i = 2
    else:
        i = i+1