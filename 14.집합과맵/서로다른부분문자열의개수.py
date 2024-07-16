S = input()
l = len(S)
sub_S = {}
for i in range(l):
    for j in range(i+1,l+1):
        sub_S[S[i:j]] = False
print(len(sub_S))