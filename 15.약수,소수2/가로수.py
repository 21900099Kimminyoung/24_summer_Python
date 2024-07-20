# 가로수의 개수를 입력받는다.
# 가로수의 위치를 입력받는다.
# dict로 위치를 입력 받아서 1부터 안에 dict안에 있는지 확인하면서 count 하기
import sys
n = int(sys.stdin.readline().strip())
l = []
new_l = []
count = 0

for i in range(n):
    num = int(sys.stdin.readline().strip())
    l.append(num)
    if i > 0:
        new_l.append(num - pre)
    pre = num
dis = min(new_l)
for i in range(n-1):
    count = count + new_l[i]//dis 
print(count)




