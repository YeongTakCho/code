import sys; input=sys.stdin.readline
import heapq

for _ in range(int(input())):
    maxH=[]
    minH=[]
    visited=[False]*1000000
    for i in range(int(input())):
        c,n=input().split()
        if c=='I':
            heapq.heappush(maxH,[-int(n),i])
            heapq.heappush(minH,[int(n),i])
            visited[i]=True
        elif n=='1':
            while maxH and not visited[maxH[0][1]]:heapq.heappop(maxH)
            if maxH:
                visited[maxH[0][1]]=False
                heapq.heappop(maxH)
        else:
            while minH and not visited[minH[0][1]]:heapq.heappop(minH)
            if minH:
                visited[minH[0][1]]=False
                heapq.heappop(minH)
    while maxH and not visited[maxH[0][1]]:heapq.heappop(maxH)
    while minH and not visited[minH[0][1]]:heapq.heappop(minH)
    if maxH:
        print(-maxH[0][0],minH[0][0])
    else:
        print('EMPTY')

#참고-https://neomindstd.github.io/%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4/boj7662/