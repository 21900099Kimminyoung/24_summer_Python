# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# sort(key = len)도 있지만 길이로 정렬하고 사전순으로 정렬하기 위해서는 다중 조건필요 => lambda
# 첫번째 기준은 길이, 두번째 기준은 사전순
# 중복되는 단어 제거 => dict.fromkeys(list), set도 있으나 순서가 변경된다.
import sys
n = int(sys.stdin.readline().strip())
S = []
for i in range(n):
    S.append(sys.stdin.readline().strip())
S.sort(key=lambda x : (len(x),x))
S = list(dict.fromkeys(S))
print(*S,sep='\n')