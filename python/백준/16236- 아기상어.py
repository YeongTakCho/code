import sys
read=sys.stdin.readline

moves=((0,1),(0,-1),(1,0),(-1,0))
data=list()
time=0

def dfs(Togo, size, visited,time):
    global data, N, moves
    finds=list()
    _Togo=list()

    time+=1

    for value in Togo:
        for move in moves:
            _y= value[0] + move[0]
            _x= value[1] + move[1]

            if _y>= 0 and _y< N and _x>= 0 and _x<N:
                if visited[_y][_x] == False:
                    if data[_y][_x] <=size:
                        visited[_y][_x]=True

                        if data[_y][_x]<size and data[_y][_x]>0:
                            finds.append((_y,_x))
                        else:
                            _Togo.append((_y,_x))
    if finds:
        return [finds,time]
    if _Togo:
        return dfs(_Togo,size,visited,time)
    else:
        return False


N=int(read())
data=[list(map(int,read().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if data[i][j]==9:
            shark=[[i,j],2,0]

while True:

    #find fish (bfs) 
    visited=[[ False for _ in range(N)] for _ in range(N)]
    visited [shark[0][0]] [shark[0][1]] =True

    dfsV = dfs([shark[0]],shark[1],visited,0)

    if dfsV:
        dfsV[0].sort(key=lambda value: (value[0],value[1]))
        time+=dfsV[1]
        data[shark[0][0]][shark[0][1]]=0
        shark[0][0]=dfsV[0][0][0]
        shark[0][1]=dfsV[0][0][1]
        shark[2]+=1
        
        if shark[1]== shark[2]:
            shark[1]+=1
            shark[2]=0

    else:
        break


print(time)


