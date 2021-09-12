import sys
testcaseNum=int(input())
m=[];n=[];x=[];y=[]
for i in range(testcaseNum):
    _m,_n,_x,_y=map(int,sys.stdin.readline().strip().split())
    m.append(_m);n.append(_n);x.append(_x);y.append(_y)
for i in range(testcaseNum):
    mset=set();nset=set()
    _m=m[i];_n=n[i];_x=x[i];_y=y[i]
    max=_m*_n
    for num in range(_x,max+1,_m):
        mset.add(num)
    for num in range(_y,max+1,_n):
        nset.add(num)
    if mset&nset:
        a=sorted(list(map(int,mset&nset)))
        print(a[0])
    else:
        print(-1)

