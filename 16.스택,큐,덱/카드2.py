# 전체 카드의 수를 입력받는다.
# 카드 수만큼 que를 생성
# n - 2 번 만큼 반복해서 첫원소 지운이후 첫원소 뒷쪽으로 넣게 첫원소 지운다.
# 원소가 2개 남았을 때 뒤의 것 출력하고 breadk

import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
card = []
for i in range(n):
    card.append(i+1)

que_card = deque(card)

while len(que_card) > 1:
    que_card.popleft()
    que_card.append(que_card.popleft())
print(que_card[0])

# input = int(input())
# square = 2

# while True:
#     if (input == 1 or input == 2):
#         print(input)
#         break
#     square *= 2
#     if (square >= input):
#         print((input - (square // 2)) * 2)
#         break
