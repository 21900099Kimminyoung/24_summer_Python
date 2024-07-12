#몇번째 순서인지 입력받는다.
#숫자를 1씩 더해가면서 str(666)이 포홤되어있으면 count++를 한다.
#count가 몇번째 순서인지와 같아지면 그만하고 결과 출력한다

n = int(input())
result = 666
count = 0
while True:
    if '666' in str(result):
        count+=1
    if count == n:
        break
    result+=1
print(result)