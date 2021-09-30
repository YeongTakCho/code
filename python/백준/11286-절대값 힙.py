import sys,heapq
read=sys.stdin.readline

n = int(read())
N=[int(read()) for _ in range(n)]
arr=list()
result=list()
for i in range(n):
    inN=N[i]
    if inN !=0:
        heapq.heappush(arr,((abs(inN),True if inN>0 else False)))
    elif inN ==0:
        if arr:
            result.append(heapq.heappop(arr))
        else:
            result.append((0,True))
for value in result:
    print(value[0] if value[1] else value[0] * -1)
