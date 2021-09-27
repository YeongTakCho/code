import sys
read=sys.stdin.readline

n,m=map(int,read().split())
passward=dict()
result=[]
for _ in range(n):
    value=read().rstrip().split(sep=' ')
    passward[value[0]]=value[1]
for _ in range(m):
    value=read().rstrip()
    result.append(passward[value])
print('\n'.join(result))