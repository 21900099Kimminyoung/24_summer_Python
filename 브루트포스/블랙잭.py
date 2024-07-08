#N개의 카드중 3장을 골라 M에 가까운 가장 큰수를 구한다.
#3중 for문을 사용한다
import sys
N, M = map(int,sys.stdin.readline().split())
card = list(map(int,sys.stdin.readline().split()))
l = len(card)
max = 0
for i in range(l-2):
    for j in range(i+1,l-1):
        for k in range(j+1,l):
            if card[i] + card[j] + card[k] > max and card[i] + card[j] + card[k] <= M:
                max = card[i] + card[j] + card[k]
print(max)
