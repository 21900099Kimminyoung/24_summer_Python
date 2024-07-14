#list 보다 dict가 가볍다..
import sys
n = int(sys.stdin.readline().strip())
names = {}
for i in range(n):
    name, record = sys.stdin.readline().split()
    if(record == 'enter'):
        names[name] = True
    else:
        del names[name]
names = list(names)
names.sort(reverse=True)
print(*names,sep='\n')