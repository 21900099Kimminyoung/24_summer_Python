import sys

while True:
    s = sys.stdin.readline().rstrip()
    bracket = []
    if s == '.':
        break
    for i in s:
        if i =='.':
            print('yse')
            break
        elif i == '[' or i == '(':
            bracket.append(i)
        elif i == ']':
            if bracket and bracket[-1] == '[':
                bracket.pop()
            else:
                print('no')
                break
        elif i == ')':
            if bracket and bracket[-1] == '(':
                bracket.pop()
            else:
                print('no')
                break
