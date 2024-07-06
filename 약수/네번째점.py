#직사각형을 만들기 위해 x, y 점이 같은 경우가 존재해야한다.
import sys
X = []
Y = []
f_x = int()
f_y = int()
for i in range(3):
    x, y = map(int,sys.stdin.readline().split())
    X.append(x)
    Y.append(y)
for i in range(3):
    if(X.count(X[i]) < 2):
        f_x = X[i]
    if(Y.count(Y[i]) < 2):
        f_y = Y[i]
print(f_x,f_y)