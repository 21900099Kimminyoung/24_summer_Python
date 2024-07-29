# 입력의 첫째 줄에는 현재 승환이의 앞에 서 있는 학생들의 수 N(1 ≤ N ≤ 1,000,자연수)이 주어진다.

# 다음 줄에는 승환이 앞에 서있는 모든 학생들의 번호표(1,2,...,N) 순서가 앞에서부터 뒤 순서로 주어진다.
# 하나의 배열 선언 => 옆라인
# curr_num = 1 로 선언
# 맨처음 번호가 1이 아니면 옆라인으로 이동 => 옆라인 배열에 저장
# 1 이후에 옆라인 배열과 원래 라인을 전부 확인
# 맞는 것을 넘긴다
# 아무리해도 맞지 않으면 Sad 출력

import sys

side = []
curr_num = 1

n = int(sys.stdin.readline().rstrip())
num = list(map(int,sys.stdin.readline().split()))

while n != curr_num:
    if num and num[0] == curr_num:
        num.pop(0)
        curr_num += 1
    elif side and side[-1] == curr_num:
        side.pop()
        curr_num += 1
    else:
        side.append(num.pop(0))
        if len(side) > 1 and side[-1] > side[-2]:
            break
if (len(num) == 1 and len(side) == 0 and num[0] == curr_num) or (len(num) == 0 and len(side) == 1 and side[0] == curr_num):
    print('Nice')
else:
    print('Sad')
    
