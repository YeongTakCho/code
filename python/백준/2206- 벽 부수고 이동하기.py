from queue import Queue
import sys;read= sys.stdin.readline

N,M = map(int,read().strip().split())
s= [list(map(int,read().strip())) for _ in range(N)]
isVisited= [[[False,False]] * M] * N
isVisited[0][0][0] = True

def bfs(start,que,isVisited):
    repeatCnt =  que.qsize()
    for i in range(repeatCnt):
        y, x, isVisitedWall= que.get()
        
        if y > 0:
            if not isVisited[y-1][x][isVisitedWall]:
                isVisited[y-1][x][isVisitedWall] = True
                
                if s[y-1][x] == 0:
                    que.put((y-1,x,isVisitedWall))
                else:
                    if isVisitedWall ==0:
                        que.put((y-1,x,1))
                    else:
                        pass
                    
        if y < N-1:
            if not isVisited[y+1][x][isVisitedWall]:
                isVisited[y+1][x][isVisitedWall] = True
                
                if s[y+1][x] == 0:
                    que.put((y-1,x,isVisitedWall))
                else:
                    if isVisitedWall ==0:
                        que.put((y+1,x,1))
                    else:
                        pass
        if x > 0:
            if not isVisited[y][x-1][isVisitedWall]:
                isVisited[y][x-1][isVisitedWall] = True
                
                if s[y-1][x] == 0:
                    que.put((y-1,x,isVisitedWall))
                else:
                    if isVisitedWall ==0:
                        que.put((y-1,x,1))
                    else:
                        pass
        if x < M-1:
            if not isVisited[y][x+1][isVisitedWall]:
                isVisited[y][x+1][isVisitedWall] = True
                
                if s[y-1][x] == 0:
                    que.put((y-1,x,isVisitedWall))
                else:
                    if isVisitedWall ==0:
                        que.put((y-1,x,1))
                    else:
                        pass
                
    bfs(start+1, que,s)


que = Queue()
que.put((0,0,0))
bfs(1,que,isVisited)

for line in isVisited:
    print(line)