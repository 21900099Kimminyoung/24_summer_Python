# 두수를 입력받는다
# 2부터 시작해서 두 수로 나눈다. 소수로만 나누면 되므로 2 3 5 7 로 보낸다.
# 정답은 맞으나 시간이 오래 걸린다.
# import sys
# n = int(sys.stdin.readline().strip())
# num = []
# for i in range(n):
#     a = list(map(int,sys.stdin.readline().split()))
#     num.append(a)
# for i in range(n):
#     cnt = 2
#     l = {}
#     while True:
#         if num[i][0]%cnt == 0 and num[i][1]%cnt == 0:
#             num[i][0] = num[i][0]//cnt
#             num[i][1] = num[i][1]//cnt
#             l.append(cnt)
#             cnt = 2
#         else:
#             if cnt == 2:
#                 cnt +=1
#             else:
#                 cnt += 2
#         if cnt > num[i][0] or cnt > num[i][1]:
#             break
#     result = num[i][0] * num[i][1]
#     for i in l:
#         result = result * i
#     print(result)

# math에 함수를 가져와서 사용
# 최소공배수 : math.lcm()
# 최대공약수 : math.gcd()
import sys
import math
n = int(sys.stdin.readline().strip())
l = []
for i in range(n):
    l.append(list(map(int,sys.stdin.readline().split())))
for i in range(n):
    print(math.lcm(l[i][0],l[i][1]))
