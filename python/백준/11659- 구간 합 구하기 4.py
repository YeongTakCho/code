import sys; read=sys.stdin.readline

N,M=map(int,read().split())
n= list(map(int,read().strip().split()))
result =[]

"""
    #try1. TC = M * N
    
    for _ in range(M): # TC= M
        i, j = map(int,read().strip().split())
        result.append(sum(n[i-1:j])) # TC= N
    for v in result:
        print(v)
"""

#try2. DP. TC= N + M
dp =[0,n[0]]

for cnt in range(1,N): # TC = N
    dp.append(dp[cnt] + n[cnt])

for _ in range(M): # TC= M
    i, j = map(int,read().strip().split())
    result.append(dp[j]- dp[i-1])
    
for v in result:
    print(v)