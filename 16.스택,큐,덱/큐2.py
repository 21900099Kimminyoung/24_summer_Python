# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# deque 사용

import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

save = deque()

for i in range(n):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        save.append(order[1])
    elif order[0] == 'pop':
        if save:
            print(save.popleft())
        else:
            print('-1')
    elif order[0] == 'size':
        print(len(save))
    elif order[0] == 'empty':
        if not save:
            print('1')
        else:
            print('0')
    elif order[0] == 'front':
        if save:
            print(save[0])
        else:
            print('-1')
    elif order[0] == 'back':
        if save:
            print(save[-1])
        else:
            print('-1')
    
