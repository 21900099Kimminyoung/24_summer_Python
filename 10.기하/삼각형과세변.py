import sys
state = ['Equilateral','Isosceles','Scalene']
cu_state = []
while True:
    num = list(map(int,sys.stdin.readline().split()))
    max_num_index = num.index(max(num))
    sum = 0
    if(num[0] == 0 and num[1] == 0 and num[2] == 0):
        break
    for i in range(3):
        if(i != max_num_index):
           sum = sum + num[i]
    if(sum <= num[max_num_index]):
        cu_state.append('Invalid')
    else:
        if(num[0] == num[1] and num[1] == num[2] and num[0] == num[2]):
            cu_state.append(state[0])
        elif(num[0] == num[1] or num[1] == num[2] or num[0] == num[2]):
            cu_state.append(state[1])
        else:
            cu_state.append(state[2])
print(*cu_state,sep='\n')

