import sys
read = sys.stdin.readline

ans=0

n,k=map(int,read().split())
coins=[int(read()) for _ in range(n)]

for i in range(n-1,-1,-1):
    while k>=coins[i]:
        ans+= ( k//coins[i] )
        k-=(coins[i] * ( k//coins[i]))
print(ans)