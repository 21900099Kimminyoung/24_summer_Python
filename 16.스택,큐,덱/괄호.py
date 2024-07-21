# 총 개수를 입력받는다
# 
import sys
n = int(sys.stdin.readline().strip())
result = []
for i in range(n):
    l = sys.stdin.readline().strip()
    check = []
    dis = len(l)
    if dis % 2 != 0:
        result.append('NO')
    else:
        for j in l:
            if j == '(':
                check.append(j)
            else:
                if check:
                    check.pop()
                else:
                    check.append(j)
                    break
        if not check:
            result.append('YES')
        else:
            result.append('NO')
print(*result,sep = '\n')

                
