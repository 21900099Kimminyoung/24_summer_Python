# # 첫 번째 줄에는 창문의 개수와 사람의 수 N(1 ≤ N ≤ 2,100,000,000)이 주어진다.
# import sys
# n = int(sys.stdin.readline().strip())
# window = [0] * (n+1)

# for i in range(1,n+1):
#     for j in range(i,n+1,i):
#         if window[j] == 0:
#             window[j] = 1
#         else:
#             window[j] = 0
# count = 0

# for i in range(1,n+1):
#     if window[i] == 1:
#         count+=1

# print(count)

## 메모리 64m가 만들어야 해서 21억개를 커버하기 쉽지 않다.
# 규칙을 찾아 제곱수이하 일때
import sys
import math
n = int(sys.stdin.readline().strip())
print(int(math.sqrt(n)))


