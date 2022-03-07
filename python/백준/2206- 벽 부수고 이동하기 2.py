# 메모리초과 or 시간초과 
# 배운 점: 자료 구조로서의 큐는 collection.deque 사용, queue를 사용할 때에는 재귀보다는 while 문을 사용하자
from collections import deque
import sys; read= sys.stdin.readline
sys.setrecursionlimit(10**7)

N, M = map(int,read().strip().split())
s= [list(map(int,read().strip())) for _ in range(N)]
isVisited = [[[False,False] for _ in range(M)] for _ in range(N)]; isVisited[0][0][0] =True
moves = ((1,0), (-1,0), (0,1), (0,-1))
que =deque([(0,0,0)])

def bfs(start, q : deque):
    q_size = len(q)
    
    for _ in range(q_size):
        y, x, isVisitedwall = q.popleft()

        for move in moves:
            my = y+ move[0]; mx = x+ move[1]
            if my>=0 and my<N and mx>=0 and mx<M and isVisited[my][mx][isVisitedwall] == False:
                if s[my][mx] == 0 and (isVisitedwall ==0 or (isVisitedwall ==1 and not isVisited[my][mx][0])):
                    isVisited[my][mx][isVisitedwall] = True
                    q.append((my,mx,isVisitedwall))
                
                elif s[my][mx] == 1 and isVisitedwall ==0 and isVisited[my][mx][1] ==False and isVisited[my][mx][0] ==False:
                    isVisited[my][mx][1] =True
                    q.append((my,mx,1))
                    
    if True in isVisited[N-1][M-1]:
        return start
    elif not q:
        return -1          
    else:
        return bfs(start+1, q)
    
print(bfs(2, que))