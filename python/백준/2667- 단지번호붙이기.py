import sys
read=sys.stdin.readline
ways=((1,0),(-1,0),(0,1),(0,-1))
def recursion(togoList):
    global Map, visited, Lines
    houses=0

    _togolist=list()
    for value in togoList:
        for way in ways:
            y=value[0]+way[0]
            x=value[1]+way[1]
            if x<Lines and x>=0 and y<Lines and y>=0:
                if visited[y][x]==False:
                    visited[y][x]=True
                    if Map[y][x]=='1':
                        _togolist.append((y,x))
                        houses+=1
            else:
                continue

    if _togolist:
        houses+= recursion(_togolist)
    return houses

Lines=int(read())
result=0
housess=list()
Map = [read().rstrip() for _ in range(Lines)]
visited=[[False]*Lines for _ in range(Lines)]

for i in range(Lines):
    for j in range(Lines):
        if visited[i][j]==False:
            visited[i][j]=True
            if Map[i][j]=='1':
                housess.append(recursion([(i,j)])+1)
                result+=1
print(result)

housess.sort()
for houses in housess:
    print(houses)