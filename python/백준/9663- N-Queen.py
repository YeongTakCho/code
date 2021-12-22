#https://www.acmicpc.net/source/36027355
N = int(input())

cnt = 0

bd = [False]*N          # idx는 j
diag1 = [False]*(2*N)   # idx는 i+j
diag2 = [False]*(2*N)   # idx는 i-j

# 다음 i번째 퀸을 j에 놓을 수 있는지 확인하는 함수.
def f(i):
    # 끝에 도달하면 종료
    if i == N:
        # print(bd)
        global cnt; cnt +=1
        return
    # 1. j값이 앞에랑 걸리는게 있는지?
    # 2. 대각선에 걸리는게 있는지?
    for j in range(N):
        if not (bd[j] or diag1[i+j] or diag2[i-j]) :
            bd[j] = diag1[i+j] = diag2[i-j] = True
            f(i+1)
            bd[j] = diag1[i+j] = diag2[i-j] = False
        
f(0)
print(cnt)