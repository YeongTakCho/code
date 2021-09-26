import sys, heapq
input=sys.stdin.readline

N=int(input())
h=list()

for _ in range(N):
    value=int(input())
    if value==0:
        if h:
            print(heapq.heappop(h)*-1)
        else:
            print(0)
    else:
        heapq.heappush(h,value*-1)
        