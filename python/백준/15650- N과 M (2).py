def dfs(start):
    if len(stack)==m:
        print(*stack)
        return
    for i in range(start,n+1):
        stack.append(i-1)
        dfs(i+1)
        stack.pop()
n,m=map(int,input().split())
stack=[]
dfs(1)