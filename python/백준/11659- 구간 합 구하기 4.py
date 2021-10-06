import sys
read=sys.stdin.readline

n,m=map(int,read().split())

result=list()


N=list(map(int,read().split()))
for _ in range(m):
    i,j=map(int,read().split())

    result.append(sum(N[i-1:j]))
for v in result:
    print(v)