import sys
#D=0, S=1, L=2, R=3
T=int(sys.stdin.readline())
for _ in range(T):
    start, end =map(int,sys.stdin.readline().split())

    history=[list() for _ in range(10000)]
    runplace=set([end])
    key=0
    while key==0:
        _runpalce=set()
        for runNum in runplace:
            __runplace=set()
            before=history[runNum] #list
            #D
            if runNum%2==0:
                if history[runNum//2]==list():
                    history[runNum//2]=before+[0]
                    __runplace.add(runNum//2)
            #S
            if runNum==9999:
                if history[0]==list():
                    history[0]=before+[1]
                    __runplace.add(0)
            elif history[runNum+1]==list():
                history[runNum+1]=before+[1]
                __runplace.add(runNum+1)
            #L
            appendNum=runNum//10 + ((runNum - (runNum//10 * 10)) * 1000)
            if history[appendNum]==list():
                history[appendNum]=before+[2]
                __runplace.add(appendNum)
            #R
            appendNum=runNum*10 - runNum//1000 * 9999
            if history[appendNum]==list():
                history[appendNum]=before+[3]
                __runplace.add(appendNum)
            if start in __runplace:
                key=1
                break
            else:
                _runpalce.update(__runplace)
        runplace=_runpalce
    for i in range(len(history[start])-1,-1,-1):
        c= history[start][i]
        if c==0:
            print('D',end='')
        elif c==1:
            print('S',end='')
        elif c==2:
            print('L',end='')
        elif c==3:
            print('R',end='')
    print()
