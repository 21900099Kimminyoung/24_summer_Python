# 세 각의 크기가 모두 60이면, Equilateral
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
# 세 각의 합이 180이 아닌 경우에는 Error
d1 = int(input())
d2 = int(input())
d3 = int(input())
if d1+d2+d3 != 180:
    print('Error')
else:
    if d1 == 60 and d2 == 60 and d3 == 60:
        print('Equilateral')
    elif d1 == d2 or d2 == d3 or d3 == d1:
        print('Isosceles')
    else:
        print('Scalene')
