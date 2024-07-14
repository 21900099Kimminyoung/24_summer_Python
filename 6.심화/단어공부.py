#단어를 입력받아서 대분자로 바꾼다
#각 단어어를 저장한단
#각 단어가 몇번 사용되느지 저장하고 가장 많이 사용되는 알바벳 출력
#여러개가 많으면 ? 출력
S = input().upper()
alphabet_list =  []
num_list = [0] * 26
for i in range(65,91):
    alphabet_list.append(chr(i))
for char in alphabet_list:
    num_list[ord(char)-65] = S.count(char)
if num_list.count(max(num_list)) > 1:
    print('?')
else:
    print(alphabet_list[num_list.index(max(num_list))])
