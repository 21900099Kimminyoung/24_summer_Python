# ax + by = c
# dx + ey = f
# 연립 방적식 풀기
# 1. a = 2 , d = 1 이라고 할때 a/d = 2 를 d에 곱하면 된다.
# 2. a/b를 e와 f에 곱한다.
# 3. b와 e를 빼고 c와 f를 뺀다.
# 4. y = (c-f) / (b-e)
# 5. x = (c-by) / a
# 6. x, y를 출력
import sys
a, b, c, d, e, f= map(int,sys.stdin.readline().split())
e = e * (a/d)
f = f * (a/d)
y = (c-f) // (b-e)
x = (c - b*y) // a
print(x,y)
# 정답....
# a, b, c, d, e, f = map(int, input().split())

# print((c*e-b*f)//(a*e-b*d), (a*f-d*c)//(a*e-b*d))