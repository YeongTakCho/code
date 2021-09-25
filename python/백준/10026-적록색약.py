import sys;input=sys.stdin.readline


B=0
R=0
G=0
RG=0

n=int(input())
colors=[input().strip() for _ in range(n)]
visited=[[0]*n for _ in range(n)]
_visited=[[0]*n for _ in range(n)] #RG용
mx=[-1,0,1,0]
my=[0,1,0,-1]
toGo=set()

for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            if colors[i][j]=='B':
                toGo.add(((i,j)))
                visited[i][j]=1
                while toGo!=set():
                    _toGo=set()
                    for Go in toGo:
                        for _i in range(4):
                            gy=my[_i]+Go[0]
                            gx=mx[_i]+Go[1]
                            if gx<0 or gx>=n or gy<0 or gy>=n:
                                continue
                            if visited[gy][gx]==0:
                                if colors[gy][gx]=='B':
                                    _toGo.add((gy,gx))
                                    visited[gy][gx]=1
                    toGo=_toGo
                B+=1
            if colors[i][j]=='R':
                toGo.add(((i,j)))
                visited[i][j]=1
                while toGo!=set():
                    _toGo=set()
                    for Go in toGo:
                        for _i in range(4):
                            gy=my[_i]+Go[0]
                            gx=mx[_i]+Go[1]
                            if gx<0 or gx>=n or gy<0 or gy>=n:
                                continue
                            if visited[gy][gx]==0:
                                if colors[gy][gx]=='R':
                                    _toGo.add((gy,gx))
                                    visited[gy][gx]=1
                    toGo=_toGo
                R+=1
            if colors[i][j]=='G':
                toGo.add(((i,j)))
                visited[i][j]=1
                while toGo!=set():
                    _toGo=set()
                    for Go in toGo:
                        for _i in range(4):
                            gy=my[_i]+Go[0]
                            gx=mx[_i]+Go[1]
                            if gx<0 or gx>=n or gy<0 or gy>=n:
                                continue
                            if visited[gy][gx]==0:
                                if colors[gy][gx]=='G':
                                    _toGo.add((gy,gx))
                                    visited[gy][gx]=1
                    toGo=_toGo
                G+=1
toGo=set()
for i in range(n):
    for j in range(n):
        if _visited[i][j]==0:
            if colors[i][j]=='G'or colors[i][j]=='R':
                toGo.add(((i,j)))
                _visited[i][j]=1
                while toGo!=set():
                    _toGo=set()
                    for Go in toGo:
                        for _i in range(4):
                            gy=my[_i]+Go[0]
                            gx=mx[_i]+Go[1]
                            if gx<0 or gx>=n or gy<0 or gy>=n:
                                continue
                            if _visited[gy][gx]==0:
                                if colors[gy][gx]=='G'or colors[gy][gx]=='R':
                                    _toGo.add((gy,gx))
                                    _visited[gy][gx]=1
                    toGo=_toGo
                RG+=1
print(R+G+B,RG+B)