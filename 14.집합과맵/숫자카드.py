# 상근이가 가지고 있는 카드수 입력받는다.
# 상근이가 가지고 있는 카드의 정보 입력 받는다.
# 전체 카드수
# 전체 카드의 정보
# 전체 카드 중 상근이가 가지고 있는 것을 출력한다.
# 전체 카드의 정보를 dic으로 만든다.
# 값들을 0으로 변경한다.
# 상근이가 가지고 있는 카드의 경우 dict의 값은 1로 변경한다.
# 전체를 출력한다.
import sys
N = int(sys.stdin.readline().strip())
N_inf = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
M_inf = list(map(int,sys.stdin.readline().split()))
M_inf = dict.fromkeys(M_inf)
for i in M_inf:
    M_inf[i] = 0
for i in N_inf:
    if i in M_inf:
        M_inf[i] = 1
for i in M_inf:
    print(M_inf[i],end=' ')

