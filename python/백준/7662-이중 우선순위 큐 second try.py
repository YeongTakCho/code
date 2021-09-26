#시간초과
import sys,heapq

input=sys.stdin.readline
T=int(input())
for _ in range(T):
    k=int(input())
    h=list()
    for __ in range(k):
        c,n=input().split();n=int(n)
        if c=='I':
            heapq.heappush(h,n)
        else:
            if h==list():
                continue
            if n==-1:
                heapq.heappop(h)
            else:
                h.remove(max(h))
                heapq.heapify(h)
    if h==list():
        print('EMPTY')
    else:
        print(max(h),min(h))
    