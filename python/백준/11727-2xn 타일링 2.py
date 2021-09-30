n=int(input())
dp=[0,1,3]
if n<=2:
    print(dp[2])
else:
    start=2
    while start<n:
        dp.append(dp[start]+dp[start-1]*2)
        start+=1
    print(dp[n])