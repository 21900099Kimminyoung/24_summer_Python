# 2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, 
# y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
# sort의 lambda사용
import sys
n = int(sys.stdin.readline().strip())
dot = []
for i in range(n):
    dot.append(list(map(int,sys.stdin.readline().split())))
dot.sort(key=lambda x:(x[1],x[0]))
for i in range(n):
    print(*dot[i])