import sys; read = sys.stdin.readline


def solution():

    # set


    n = int(read())
    grape = [[0]*n]*n
    setList = [set() for _ in range(n)]

    # input


    for p in range(n):
        i=0
        for inC in read().split():
            if inC == '1':
                setList[p].add(i)
            i+=1

    #solve

    def recursion(n,visited):
        for v in setList[n]:
            if visited[v]==False:
                
        
        
    for i in range(n):
        clearVisited=[False]*n
        clearVisited[i]=True
        recursion(i,clearVisited)

    #output

    for i in range(n):
        print(*grape[i], sep=' ')



solution()