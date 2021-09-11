n,m=map(int,input().split())
listTree=list(map(int,input().split()))
lenTree=max(listTree)
minusnum=1
key=0

def getTree(listTree,lenTree):
    Trees=0
    for Tree in listTree:
        if Tree>lenTree:
            Trees+=(Tree-lenTree)
    return Trees

while True:
    getT=getTree(listTree,lenTree)
    if getT==m: 
        break
    elif getT<m:
        lenTree-=minusnum
        minusnum*=2
    else:
        minusnum/=2
        lenTree +=minusnum
        break

while True:
    getT=getTree(listTree,lenTree)
    if getT==m:
        break
    elif getT<m:
        lenTree-=minusnum
        if minusnum==1 and getTree(listTree,lenTree)!=m:
            lenTree-=1
            break
        minusnum/=2

    else:
        lenTree +=minusnum*2
print(int(lenTree))