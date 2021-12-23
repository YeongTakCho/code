#시간초과
import sys
read = sys.stdin.readline

def sol():
    N= int(read())
    stair = [int(read()) for _ in range(N)]
    stair.reverse(); stair= stair + [False]* 2
    def dfs(n,wasOnestep,val):
        if not stair[n]:
            return val
        else:         
            if wasOnestep:
                return dfs(n+2,False, val+ stair[n])
            else:
                return max([dfs(n+2,False, val+ stair[n]), dfs(n+1, True, val+ stair[n])])
    return dfs(0,False,0)

print(sol())