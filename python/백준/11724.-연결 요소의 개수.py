import sys;input=sys.stdin.readline

n,m=map(int,input().split())
lineDict=dict()
for _ in range(m):
    p1,p2=map(int,input().split())
    try:
        lineDict[p1].add(p2)
    except:
        lineDict[p1]=set([p2])
    try:
        lineDict[p2].add(p1)
    except:
        lineDict[p2]=set([p1])
_visited=lineDict.keys()
visited=dict()
for num in _visited:
    visited[num]=0


total=0
for key in _visited:
    if visited[key]==1:
        continue
    total+=1
    visited[key]=1
    goList=list()
    for num in lineDict[key]:
        if visited[num]==0:
            visited[num]=1
            goList.append(num)
    while goList!=list():
        _goList=list()
        for go in goList:
            for num in lineDict[go]:
                if visited[num]==0:
                    visited[num]=1
                    _goList.append(num)
        goList=_goList
print(total+(n-len(lineDict.keys())))
#https://www.acmicpc.net/source/33701114