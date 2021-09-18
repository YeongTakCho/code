import sys,copy
T=int(sys.stdin.readline())
for _ in range(T):
    history=dict()
    start,end=map(int,sys.stdin.readline().split())
    history['']=set([end])

    while True:
        key=0
        _history=dict()
        #D part
        for key in history.keys():
            appendSet=set()
            for num in history[key]:
                if num%2==0:
                    appendSet.add(num//2+500)
                    appendSet.add(num//2)
            if appendSet!=set():
                if start in appendSet:
                    print('D'+key)
                    key=1
                    break
                _history['D'+key]=appendSet
        if key==1:
            break
        #S part
        for key in history.keys():
            appendSet=set()
            for num in history[key]:
                if num==9999:
                    appendSet.add(0)
                else:
                    appendSet.add(num+1)
            if start in appendSet:
                print('S'+key)
                key=1
                break
            _history['S'+key]=appendSet
        if key==1:
            break
        #R part
        for key in history.keys():
            appendSet=set()
            for num in history[key]:
                appendSet.add(num*10 - num//1000 * 9999)
            if start in appendSet:
                print('R'+key)
                key=1
                break
            _history['R'+key]=appendSet
        if key==1:
            break

        #L part
        for key in history.keys():
            appendSet=set()
            for num in history[key]:
                appendSet.add(num//10 + ((num - (num//10 * 10)) * 1000))
            if start in appendSet:
                print('L'+key)
                key=1
                break
            _history['L'+key]=appendSet
        if key==1:
            break
        history=copy.deepcopy(_history)
        
        
