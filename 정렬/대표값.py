import sys
n = []
for i in range(5):
    n.append(int(sys.stdin.readline()))
avg = int(sum(n) / 5)
n.sort()
print(avg)
print(n[2])