import sys; read=sys.stdin.readline
n,m=map(int,read().split())
list1=[read().rstrip() for _ in range(n)]
list2=[read().rstrip() for _ in range(m)]
unionList=set(list1).intersection(set(list2))
print(len(unionList))
for name in sorted(list(unionList)):
    print(name)