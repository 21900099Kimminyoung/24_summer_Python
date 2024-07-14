# cloud3.5가 생성한 코드
#  import sys

# n = int(sys.stdin.readline().strip())
# grid = [[0] * 100 for _ in range(100)]  # 100x100 격자 생성

# # 각 사각형을 격자에 표시
# for _ in range(n):
#     x, y = map(int, sys.stdin.readline().split())
#     for i in range(x, min(x+10, 100)):
#         for j in range(y, min(y+10, 100)):
#             grid[i][j] = 1

# # 격자에서 1로 표시된 칸의 수를 세기
# total_area = sum(sum(row) for row in grid)

# print(total_area)

import sys
n = int(sys.stdin.readline().strip())
grid = [[0 for j in range(100)] for i in range(100)]
for i in range(n):
    A, B = map(int,sys.stdin.readline().split())
    for k in range(A,A+10):
        for l in range (B,B+10):
            grid[k][l] = 1
print(sum(sum(row) for row in grid))