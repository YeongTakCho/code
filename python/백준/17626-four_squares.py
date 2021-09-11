n=int(input())
getMaxRoot=lambda x: int(x**0.5)
getLowRoot=lambda x: int((x**0.5)/2)+1

def getSquareNum(num,upFloor,seq):
    if num==0:
        return seq
    elif seq==3:
        return 4

    returns=set()

    getMax=getMaxRoot(num)
    if getMax>upFloor:
        getMax=upFloor
    getLow=getLowRoot(num)
    for i in range(getLow,getMax+1):
        returns.add(getSquareNum(num-i**2,i,seq+1))
    return min(returns)

print(getSquareNum(n,getMaxRoot(n),0))

