#heapq 사용한 풀이
import sys; read= sys.stdin.readline
import heapq
INF = sys.maxsize

def sol():
    #꼭짓점 갯수와 모서리 갯수 입력
    nVertex, nExcreta = map(int,read().split())
    #시작점 (0부터 시작)
    s= int(read()) -1 

    dist=[INF for _ in range(nVertex)]; dist[s] = 0
    graph = [[] for _ in range(nVertex)]
    
    for _ in range(nExcreta):
        u, v, w= map(int,read().split())    
        graph[u-1].append((v-1,w))
        
    def dijkstra(start):
        heap=[]
        heapq.heappush(heap,(0,start))  
                
        while heap:
            wei, now= heapq.heappop(heap)
            
            if dist[now] < wei:
                continue
            
            else:
                dist[now]  = wei
                for nextNode, w in graph[now]:
                    nextwei = w + dist[now]
                    if dist[nextNode] < nextwei:
                        continue
                    else:
                        dist[nextNode] = nextwei
                        heapq.heappush(heap,(nextwei, nextNode))
    dijkstra(s)
    return dist     
        
    
arr = sol()
for val in arr:
    if val == INF:
        print('INF')
    else:
        print(val)