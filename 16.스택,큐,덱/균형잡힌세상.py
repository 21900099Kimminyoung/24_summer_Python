# 문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고, 문자열이 균형을 이루는 조건은 아래와 같다.

# 모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
# 모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
# 모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
# 모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
# 짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.
# (, [ 를 저장할 list를 선언한다.
# 계속해서 문자열을 입력받는다.
# 문자열이 . 이면 반복문을 나온다.
# 문자열에서 (, [ 이면 계속해서 배열에 저장한다.
# )이 나왔을 때 list의 top이 ( 이고 list가 비어있지 않으면 맨위의 것을 지운다.
# [이 나왔을 때 list의 top가 ] 이고 list가 비어있지 않으면 맨위의 것을 지운다.
# 아니라면 list에 현재 문자열을 넣고 break

# list가 비어있으면 yes
# 아니라면 no
import sys

while True:
    s = sys.stdin.readline().rstrip()
    bracket = []
    if s == '.':
        break
    else:
        for i in s:
            if i == '(' or i == '[':
                bracket.append(i)
            elif i == ']':
                if bracket and bracket[-1] == '[':
                    bracket.pop()
                else:
                    bracket.append(i)
                    break
            elif i == ')':
                if bracket and bracket[-1] == '(':
                    bracket.pop()
                else:
                    bracket.append(i)
                    break
        if bracket:
            print('no')
        else:
            print('yes')
        
    