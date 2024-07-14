import sys
n = list(map(int,sys.stdin.readline().split()))
max_num_index = n.index(max(n))
sum = 0
for i in range(3):
    if(i != max_num_index):
        sum = sum + n[i]
if(sum == n[max_num_index]):
    sum = sum -1
elif(sum < n[max_num_index]):
    n[max_num_index] = n[max_num_index] - (n[max_num_index] - sum + 1)
sum = sum + n[max_num_index]
print(sum)
