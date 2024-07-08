# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 1
#         for j <- i + 1 to n
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }
# i = 1 (n-1)
# i = 2 (n-2)
# i = n-1 1
# (n-1)(n)/2
import math
n = int(input())
print(int(n/2*(n-1)))
print(2)