# 첫째 줄에는 영수증에 적힌 총 금액 
# 둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 
# 이후 줄에는 각 물건의 가격 개수
total = int(input())
n = int(input())
sum = 0
for i in range(n):
    a, b = map(int,input().split())
    sum = sum + a*b
if sum == total:
    print("Yes")
else:
    print("No")