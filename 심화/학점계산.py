#  과목명, 학점, 등급이 공백으로 구분되어 주어진다.
import sys
score = ['A+','A0','B+','B0','C+','C0','D+','D0','F','P']
obj = []; H = []; Grade = [];count = 0
for i in range(20):
    a, b, c = sys.stdin.readline().strip().split()
    obj.append(a)
    H.append(b)
    Grade.append(c)
H = list(map(float,H))
totol = 0.0; totol_sum = 0
for i in range(20):
    if(Grade[i]==score[0]):
        totol = totol + H[i]*4.5
    elif(Grade[i]==score[1]):
        totol = totol + H[i]*4.0
    elif(Grade[i]==score[2]):
        totol = totol + H[i]*3.5
    elif(Grade[i]==score[3]):
        totol = totol + H[i]*3.0
    elif(Grade[i]==score[4]):
        totol = totol + H[i]*2.5
    elif(Grade[i]==score[5]):
        totol = totol + H[i]*2.0
    elif(Grade[i]==score[6]):
        totol = totol + H[i]*1.5
    elif(Grade[i]==score[7]):
        totol = totol + H[i]*1.0
    if(Grade[i]!=score[9]):
        totol_sum = totol_sum + H[i]
print(totol/totol_sum)