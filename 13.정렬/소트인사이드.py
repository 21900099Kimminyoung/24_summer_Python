N = input()
N = list(map(int,N))
N.sort(reverse=True)
print(*N,sep='')