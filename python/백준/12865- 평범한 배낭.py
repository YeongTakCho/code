import sys; read= sys.stdin.readline

N,K = map(int,read().strip().split())
s= [list(map(int,read().strip().split())) for _ in range(N)]
dp = [0] * (K+1)

for w, v in s:
    for cnt in range(K- w, -1, -1):
        if dp[cnt] + v > dp[cnt+ w]:
            dp[cnt + w] = dp[cnt] + v

print(dp[K])