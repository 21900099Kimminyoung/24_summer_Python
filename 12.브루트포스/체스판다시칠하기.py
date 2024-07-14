import sys
N, M = map(int,sys.stdin.readline().split())
m = list()
err = []
for i in range(N):
    line = sys.stdin.readline().strip()
    m.append(list(line))
for i in range(N - 7):
    for j in range(M -7):
        re1 = 0
        re2 = 0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k + l) % 2 == 0:
                    if(m[k][l] != 'W'):
                        re1+=1
                    if(m[k][l] != 'B'):
                        re2+=1
                else:
                    if(m[k][l] != 'B'):
                        re1+=1
                    if(m[k][l] != 'W'):
                        re2+=1
        err.append(re1)
        err.append(re2)
print(min(err))

                
