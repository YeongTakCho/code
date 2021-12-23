#참고 알고리즘: https://namu.wiki/w/%EC%B5%9C%EC%9E%A5%20%EC%A6%9D%EA%B0%80%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4
def sol():
    N = int(input())
    A = [0] + list(map(int,input().split()))
    D = [0]+ [None] * N
    MAX = 0

    for i in range(1,N+1):
        if A[i] > D[MAX]:
            D[MAX+1] = A[i]
            MAX += 1
        else:
            for index in range(1,MAX+1):
                if A[i] <= D[index]:
                    D[index] = A[i]
                    break
    return MAX

print(sol())