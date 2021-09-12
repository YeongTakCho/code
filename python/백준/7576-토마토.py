import sys

M,N=map(int,sys.stdin.readline().strip().split())
tomato=[]
checklist=[]
Stop=0

for i in range(N):
    appendList=(list(map(int,sys.stdin.readline().strip().split())))
    tomato.append(appendList)
    if 0 in appendList:
        checklist.append(0)
    else:
        checklist.append(1)
def findTomato():
    global tomato,M,N
    returnList=[]
    for n in range(N):
        for m in range(M):
            if tomato[n][m]==1:
                returnList.append([n,m])
    return returnList

def putTomato(tomatoState):
    global tomato,M,N,Stop
    Stop=1
    moveList=[[1,0],[-1,0],[0,1],[0,-1]]
    inRange=lambda small,big: True if small>=0 and small<big else False
    for tomato1 in tomatoState:
        for move in moveList:
            if inRange(tomato1[0]+move[0],N) and inRange(tomato1[1]+move[1],M):
                if tomato[tomato1[0]+move[0]][tomato1[1]+move[1]]==0:
                    tomato[tomato1[0]+move[0]][tomato1[1]+move[1]]=1
                    Stop=0
                
def docheckList():
    global tomato,N,checklist
    for i in range(N):
        if 0 in tomato[i]:
            checklist[i]=0
        else:
            checklist[i]=1
total=0
while 0 in checklist:
    tomatoState=findTomato()
    putTomato(tomatoState)
    if Stop==1:
        total=-1
        break
    docheckList()
    total+=1
print(total)