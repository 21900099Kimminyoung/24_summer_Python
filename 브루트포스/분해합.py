#N을 입력받는다
# N까지 반복하면서 tempd이 10보다 클때 일때마다 sum에 temp/10더하기 temp = 0으로
# 계속해서 sum과 temp를 더해서 N 인지 확인
N = int(input())
for i in range(1,N+1):
    s = str(i)
    temp = i
    sum = 0
    for j in range(len(s)-1):
        k = int(i/(10**(j+1)))
        sum = sum + k
        temp = temp - k*(10**(j+1))
    if(sum + temp + i == N):
        print(i)
        break