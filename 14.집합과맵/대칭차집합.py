#집합 A와 B의 개수를 입력받는다.
#집합 A와 B를 dict로 입력받는다. => value는 true
# 집합 B의 원소가 A에 있으면 A에서 value => false
# 집합 A의 원소가 B에 있으면 B에서 value => false
# true일때만 count +=1 한다.
import sys
N, M = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))
A = dict.fromkeys(A,True)
B = dict.fromkeys(B,True)
for i in A:
    if i in B:
        A[i] = False
for i in B:
    if i in A:
        B[i] = False
count = 0
for i in A:
    if A[i] == True:
        count += 1
for i in B:
    if B[i] == True:
        count += 1
print(count)