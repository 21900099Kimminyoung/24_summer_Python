# c, s, z 일때 = 인지
# d, z, = 인지
# c, d 일때 - 인지
#l, n일때 j 인지
S = input()
croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for char in croatia:
    S = S.replace(char,'*')
print(len(S))