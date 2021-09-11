import sys
comNum=int(input())
links=int(input())
comLinks=[[] for _ in range(comNum)]
comLinksCheck=[0 for _ in range(comNum)];comLinksCheck[0]=1
for i in range(links):
    n,m=map(int,sys.stdin.readline().strip().split())
    comLinks[n-1].append(m)
    comLinks[m-1].append(n)
def goLinks(start):
    global comLinks, comLinksCheck
    for links in comLinks[start-1]:
        if comLinksCheck[links-1]==0:
            comLinksCheck[links-1]=1
            goLinks(links)
goLinks(1)
print(sum(comLinksCheck)-1)