#바구니의 개수와 넣은 공을 넣는 횟수를 입력받는다.
# 0이 들어있는 바구니 N개를 만든다.
# M 번 반복하면서 ijk를 ㄷ입력받는다.
# 두번째 줄입력부터는 i j k로 이루어져 있으며, 
# i번 바구니부터 j번 바구니까지에 k번 번호가 적혀져 있는 공을 넣는다는 뜻이다.
# 바구니에 이미 공이 들어있으면 바꾼다
import sys
N, M = map(int,input().split())
basket = [0]*N
for i in range(M):
    start, end, ball_num = map(int,sys.stdin.readline().split())
    for j in range(start-1, end):
        basket[j] = ball_num
print(*basket)