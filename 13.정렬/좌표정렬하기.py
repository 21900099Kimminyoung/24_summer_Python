# 좌표의 개수를 입력 받는다.
# x 좌표를 기준으로하고 x 좌표가 같으면 y 좌표를 기준으로
# sort, sorted 사용 => lambda 사용, 다중 조건도 가능하다.
import sys
n = int(sys.stdin.readline().strip())
dot = []
for i in range(n):
    dots = list(map(int,sys.stdin.readline().split()))
    dot.append(dots)
dot.sort(key=lambda x:(x[0],x[1]))
for i in range(n):
    print(*dot[i])