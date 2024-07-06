# 좌표의 개수를 입력받는다
# x, y 좌표를 각각 입력받아서 저장한다
# 만약 좌표의 개수가 1개라면 넓이는 0이다.
# 저장된 x 좌표의 max값에서 min 값을 뺀다 -> 가로축
# 저장된 y 좌표의 max값에서 min 값을 뺀다 -> 세로축 
# 곱한 것을 프린트한다.
import sys
n = int(sys.stdin.readline().strip())
X = []; Y = []
w = 0; h = 0
for i in range(n):
    x, y = map(int,sys.stdin.readline().split())
    X.append(x)
    Y.append(y)
if n < 2:
    print(0)
else:
    w = max(X) - min(X)
    h = max(Y) - min(Y)
    print(w*h)
        
