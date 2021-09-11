import sys

checkDic_dfs=dict()
checkDic_bfs=dict()
linksDic=dict()
stacks=list()

n,m,v=map(int,input().strip().split())

for i in range(m):
    n1,n2=map(int,sys.stdin.readline().strip().split())
    checkDic_dfs[n1]=0
    checkDic_dfs[n2]=0

    try:
        linksDic[n1]=linksDic[n1]+[n2]
    except:
        linksDic[n1]=[n2]
    try:
        linksDic[n2]=linksDic[n2]+[n1]
    except:
        linksDic[n2]=[n1]
checkDic_bfs=checkDic_dfs.copy()

for key in linksDic.keys():
    linksDic[key]=sorted(list(set(linksDic[key])))

def goLinks_dfs(start):
    global checkDic_dfs, linksDic
    try:
        for links in linksDic[start]:
            if checkDic_dfs[links]==0:
                checkDic_dfs[links]=1
                print(links,end=' ')
                goLinks_dfs(links)
    except:
        pass
checkDic_dfs[v]=1
print(v,end=' ')
goLinks_dfs(v)
print()

stacks.append(v)
checkDic_bfs[v]=1
while 0 in checkDic_bfs.values():
    for stack in stacks:
        print(stack, end=' ')
        try:
            for link in linksDic[stack]:
                if checkDic_bfs[link]==0:
                    checkDic_bfs[link]=1
                    stacks.append(link)
        except:
            key=1
    if key==1:
        break
    
    