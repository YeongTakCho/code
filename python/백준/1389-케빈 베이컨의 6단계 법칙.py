import sys
n,m=map(int,sys.stdin.readline().split())
friendList=[set() for _ in range(n)]
for _ in range(m):
    n1,n2=map(int,sys.stdin.readline().split())
    friendList[n1-1].add(n2)
    friendList[n2-1].add(n1)

smallestKM=n
smallestKBN=n*n
visited=set([i+1 for i in range(n)])

for i in range(n):
    num=i+1
    KBN=0

    NotVisited=visited-set([num])
    toGo=friendList[num-1]
    voidSet=set()
    plusNum=1
    while NotVisited!=voidSet:
        _toGo=set()
        for goNum in toGo:
            if goNum in NotVisited:
                NotVisited=NotVisited-set([goNum])
                KBN+=plusNum
                for n in friendList[goNum-1]:
                    _toGo.add(n)
        toGo=_toGo
        plusNum+=1


    if KBN<smallestKBN:
        smallestKBN=KBN
        smallestKB=num
print(smallestKB)