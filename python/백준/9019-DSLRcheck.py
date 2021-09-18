import sys
def DSLR(end):
    try:
        history=[list() for _ in range(10000)]
        runplace=set([end])
        max=10000
        start=0
        while start<=max:
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
                if runNum==9999 and history[0]==list():
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
                
                _runpalce.update(__runplace)
            start+=1
            runplace=_runpalce
            if list() not in history:
                break
        for i in range(10000):
            if history[i]==list():
                print(i,end)
        print('%d finish'%end)
    except:
        print()
DSLR(9999)
