# 첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.
# 둘째 줄부터 M개의 줄에는 바구니의 순서를 역순으로 만드는 방법이 주어진다. 
# 방법은 i j로 나타내고, 왼쪽으로부터 i번째 바구니부터 j번째 바구니의 순서를 
# 역순으로 만든다는 뜻이다. (1 ≤ i ≤ j ≤ N)
# n m 을 입력받는다. n 개의 방을 가지는 list를 만들고 안에 바구니 번호를 넣는다.
# m 번 반복하면서 바구니 번호를 바꾸어 준다.(reverse 함수)
import sys
N, M  = map(int,sys.stdin.readline().split())
list = list(range(1,N+1))
for i in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    list[n1-1:n2] = list[n1-1:n2][::-1]
print(*list)