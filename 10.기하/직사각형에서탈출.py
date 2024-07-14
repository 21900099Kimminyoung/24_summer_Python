import sys
distance = []
x,y,w,h = map(int,sys.stdin.readline().split())
distance.append(abs(x-0))
distance.append(abs(x-w))
distance.append(abs(y-0))
distance.append(abs(y-h))
print(min(distance))