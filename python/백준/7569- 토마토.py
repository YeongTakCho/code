import sys
read=sys.stdin.readline
sys.setrecursionlimit(10**9)

togo=list()
turn =0
ways=((0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0))
EveryTomatoIsFine = True

M,N,H=map(int,read().split())

data=[[list(map(int,read().split())) for _ in range(N)] for _ in range(H) ]


for h in range(H):
    for n in range(N):
        for m in range(M):
            if data[h][n][m]==1:
                togo.append((h,n,m))
def dfs(togo):
    global ways,data,turn,M,N,H

    _togo=list()
    for value in togo:
        for way in ways:
            _h=value[0]+way[0]
            _n=value[1]+way[1]
            _m=value[2]+way[2]
            if _h>=0 and _h<H and _n>=0 and _n<N and _m>=0 and _m<M:
                if data[_h][_n][_m]==0:
                    data[_h][_n][_m]=1
                    _togo.append((_h,_n,_m))
            else:
                continue

    if not _togo:
        return
    else:
        turn +=1
        dfs(_togo)

dfs(togo)


for h in range(H):
    for n in range(N):
        for m in range(M):
            if data[h][n][m] ==0:
                EveryTomatoIsFine=False

if EveryTomatoIsFine:
    print(turn)
else:
    print(-1)
