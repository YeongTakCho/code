import sys
n=int(input())
timeList=list(map(int,sys.stdin.readline().strip().split()))
timeList.sort()
totalTime=0
for i in range(n):
    totalTime+=timeList[i]*(n-i)
print(totalTime)