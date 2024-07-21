# stack = []
# 1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
# append
# 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# if stack.isEmpty()  => else : stack.top.pop(-1)
# 3: 스택에 들어있는 정수의 개수를 출력한다.
# len(stack)
# 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
# if stack.isEmpty()  => else : stack.top[-1]
# 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다
import sys
n = int(sys.stdin.readline().strip())
l = []
for i in range(n):
    order = list(map(int,sys.stdin.readline().split()))
    if order[0] == 1:
        l.append(order[1])
    elif order[0] == 2:
        if len(l) == 0:
            print(-1)
        else:
            print(l[-1])
            l.pop()
    elif order[0] == 3:
        print(len(l))
    elif order[0] == 4:
        if len(l) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 5:
        if len(l) == 0:
            print(-1)
        else:
            print(l[-1])