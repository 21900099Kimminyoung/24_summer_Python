#문자열을 입력받은 그대로 출력하기
import sys
Str = []
while True:
    S = sys.stdin.readline().strip()
    if S == '':
        break;
    Str.append(S)
print(*Str,sep="\n")