#N을 입력받는다
# N까지 반복하면서 tempd이 10보다 클때 일때마다 sum에 temp/10더하기 temp = 0으로
# 계속해서 sum과 temp를 더해서 N 인지 확인
N = int(input())
for i in range(1,N+1):
    num = sum(map(int,str(i)))
    if(i + num == N):
        print(i)
        break
    if(N == i):
        print(0)
