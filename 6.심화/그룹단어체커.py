#단어를 몇개 입력받을 지 입력받는다.
#여러개의 단어를 입력받는다.
#count = 0
#입력받은 단어의 첫글자를 새로운 배열에 저장
#입력받은 단어의 이전 알바벳과 현재 알파벳이 동인한지 확인
# 동일하면 넘어가기
# 다르다면 새로운 배열에 이전과 다른 알바벳이 있는지 확인 => 있으면 check = 1 즉 그룹단어가 아니다.
import sys
n = int(input())
count = 0; uni = []; W = []; pre = ''
for i in range(n):
    S = sys.stdin.readline().strip()
    W.append(S)
for i in range(n):
    count = count + 1
    for j in range(len(W[i])):
        if(pre != W[i][j]):
            if uni.count(W[i][j]) > 0:
                count = count - 1
                break
        uni.append(W[i][j])
        pre = W[i][j]
    pre = ''
    uni = []
print(count)
    
