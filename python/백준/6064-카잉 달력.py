import sys
testcaseNum=int(input())
m=[];n=[];x=[];y=[]
for i in range(testcaseNum):
    _m,_n,_x,_y=map(int,sys.stdin.readline().strip().split())
    m.append(_m);n.append(_n);x.append(_x);y.append(_y)
for testcase in range(testcaseNum):
    key=0
    _m=m[testcase];_n=n[testcase];_x=x[testcase];_y=y[testcase]
    max= int(_m*_n/2) if _m*_n%2==0 else _m*_n
    for num in range(1,max+1):
        if num%_m==_x and num%_n==_y:
            print(num)
            key=1
            break
    if key==0:
        print(-1)
