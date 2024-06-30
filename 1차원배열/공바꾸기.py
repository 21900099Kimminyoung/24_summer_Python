# 도현이는 바구니를 총 N개 가지고 있고,
# 각각의 바구니에는 1번부터 N번까지 번호가 매겨져 있다. 바구니에는 공이 1개씩 들어있고,
# 처음에는 바구니에 적혀있는 번호와 같은 번호가 적힌 공이 들어있다.
# N, M을 입력받고 N길이의 배열을 만들고 번호에 맞는 공을 넣어준다.
# M 번 반복하면서 값을 바꾸어준다.
import sys
N, M = map(int,input().split())
basket = list(range(1,N+1))
for i in range(M):
    n1, n2 = map(int,sys.stdin.readline().split())
    basket[n1-1], basket[n2-1] = basket[n2-1], basket[n1-1]
print(*basket)