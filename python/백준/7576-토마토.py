import sys
M,N=map(int,sys.stdin.readline().strip().split())
box=[];tomatoState=[]
zeroNum=0;stop=0
ii=0
for i in range(N):
    appendList=(list(map(int,sys.stdin.readline().strip().split())))
    box.append(appendList)
    for i in range(M):
        appendNum=appendList[i]
        if appendNum==1:
            tomatoState.append([ii,i])
        elif appendNum==0:
            zeroNum+=1
    ii+=1
def putTomato():
    global box,M,N,stop,zeroNum,tomatoState
    _tomatoState=[]
    checkState=lambda n,m:True if n>=0 and m>=0 and n<N and m<M else False
    stop=1
    moveList=[[1,0],[-1,0],[0,1],[0,-1]]
    for tomato in tomatoState:
        for move in moveList:
            movedN=tomato[0]+move[0]; movedM=tomato[1]+move[1]
            if checkState(movedN,movedM):
                inbox=box[movedN][movedM]
                if inbox==0:
                    box[movedN][movedM]=1
                    _tomatoState.append([movedN,movedM])
                    zeroNum-=1
                    stop=0
    tomatoState=_tomatoState
total=0
while zeroNum>0:
    putTomato()
    if stop==1:
        total=-1
        break
    total+=1
print(total)