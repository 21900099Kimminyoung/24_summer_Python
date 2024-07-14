S = input()
check = 1
for i in range(int(len(S)/2)):
    if(S[i] != S[len(S)-i-1]):
        check = 0
print(check)