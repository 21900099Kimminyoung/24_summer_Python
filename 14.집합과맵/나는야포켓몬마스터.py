# 총 포켓몬의 수와 내가 맞추어야 하는 포켓몬의 수를 입력받는다.
# # 포케몬들의 이름을 입력받는다.
# 입력받는 번호나 포켓몬이름을 가지고 번호나 이름을 출력한다.
import sys
N, M = map(int,sys.stdin.readline().split())
names = {}
oreder = {}
for i in range(N):
    name = sys.stdin.readline().strip()
    names[name] = i + 1
    oreder[i+1] = name
for i in range(M):
    s = sys.stdin.readline().strip()
    if(s.isdigit()):
        s = int(s)
        print(oreder[s])
    else:
        print(names[s])
