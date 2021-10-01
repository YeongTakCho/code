import sys,heapq
read = sys.stdin.readline

def solution():
    h=list()
    n=int(read())
    for _ in range(n):
        inN=int(read())

        if inN:
            heapq.heappush(h,(abs(inN),inN))
        else:
            if h:
                print(heapq.heappop(h)[1])
            else:
                print(0)
solution()