from sys import stdin
read=stdin.readline
T=int(input())
for t in range(T):
    _dict=dict()
    K=int(read().strip())
    biggest=None;smallest=None
    for k in range(K):
        command, num = read().split(); num=int(num)
        if command=='I':
            try:
                _dict[num]+=1
            except:
                _dict[num]=1
            try:
                if num>biggest:
                    biggest=num
            except:
                biggest=num
            try:
                if num<smallest:
                    smallest=num
            except:
                smallest=num

        else:
            try:
                if num==1:
                    if _dict[biggest]==1:
                        del(_dict[biggest])
                        biggest=max(_dict.keys())
                    else:
                        _dict[biggest]-=1
                else:
                    if _dict[smallest]==1:
                        del(_dict[smallest])
                        smallest=min(_dict.keys())
                    else:
                        _dict[smallest]-=1
            except:
                biggest=None
                smallest=None
    if biggest==None:
        print('EMPTY')
    else:
        print(biggest,smallest)
    

