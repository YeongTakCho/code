n=int(input())
dp=[0,1,2]
if n<=2:
    print(dp[n])
else:
    start=2
    while start<n:
        dp.append(dp[start]+dp[start-1])
        start+=1
    print(dp[n]%10007)