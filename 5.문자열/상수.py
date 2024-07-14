#두개의 3자리 숫자를 입력받는다
#입력받은 세자리 수의 자리수를 반대로 변경한다
#변경한 수 중에서 큰수를 출력한다.
N, M = input().split()
N = N[::-1]; M = M[::-1]
N = int(N); M = int(M)
print(N if N > M else M)