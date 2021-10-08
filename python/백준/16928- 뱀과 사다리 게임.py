import sys


import sys
read=sys.stdin.readline

N,M=map(int,read().split())
inputs=[list(map(int,read().split())) for _ in range(N+M)]
ways=dict()

for value in inputs:
    ways[value[0]]=value[1]

dp=[1]
visited=[False]*100
visited[0]=True
turn =0

while True:
    _dp=list()

    turn +=1
    isBreak=0

    for value in dp:
        for i in range(1,7):
            if visited[value+i-1]==False:
                if value+i == 100:
                    isBreak=1
                    break
                visited[value+i-1]=True
                try:    
                    _dp.append(ways[value+i])
                except:
                    _dp.append(value+i)
    if isBreak==1:
        break
    dp=_dp
print(turn)
