n,k=map(int,input().split())
dp=[set([k]),set()]
visited=set([k])
second=0
key=0
if n==k:
    print(0)
else:
    while True:
        for i in range(2):
            _i=0 if i==1 else 1
            dp[_i]=set()
            for v in dp[i]:
                if v%2==0:
                    dp[_i].add(v//2)
                dp[_i].add(v-1)
                dp[_i].add(v+1)
            dp[_i]=dp[_i].difference(visited)
            second+=1
            if n in dp[_i]:
                key=1
                break
            visited.update(dp[_i])
        if key==1:
            break
    print(second)