# 첫째 줄에는 응시자의 수 N과 상을 받는 사람의 수 k가 공백을 사이에 두고 주어진다.
# 둘째 줄에는 각 학생의 점수 x가 공백을 사이에 두고 주어진다.
import sys
N, k = map(int,sys.stdin.readline().split())
s = list(map(int,sys.stdin.readline().split()))
s.sort(reverse=True)
print(s[k-1])