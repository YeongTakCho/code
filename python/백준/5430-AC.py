import sys
testcase=int(input())
commandss=[];numlens=[];numss=[]
for i in range(testcase):
    commandss.append(sys.stdin.readline().strip())
    numlens.append(int(sys.stdin.readline().strip()))
    inputnums=sys.stdin.readline().strip()
    inputnums=inputnums.replace('[','');inputnums=inputnums.replace(']','')
    try:
        numss.append(list(map(int,inputnums.split(','))))
    except:
        numss.append(list())
