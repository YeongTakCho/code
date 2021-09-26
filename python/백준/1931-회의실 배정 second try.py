import sys
input=sys.stdin.readline

n=int(input())
inputs=tuple(tuple(map(int,input().split())) for _ in range(n))
maxStart=max(inputs,key=lambda x: x[0])
arr=[None]*(maxStart[0]+1)
sameValue=0
same=list()
adrs=list()
for value in inputs:
    
    if value[0]==value[1]:
        sameValue+=1
        same.append(value[0])
    elif arr[value[0]] ==None:
        arr[value[0]]=value[1]
    elif value[1]<arr[value[0]]:
        arr[value[0]]=value[1]
    else:
        continue
_max=maxStart[1]
adrs.append(maxStart[0])
for i in range(maxStart[0]-1,-1,-1):
    if arr[i]==None:
        continue
    if arr[i]>=_max:
        arr[i]=None
    else:
        _max=arr[i]
        for sameNum in same:
            if sameNum<arr[i] and sameNum>i:
                arr[i]=None
                break
    if arr[i] != None:
        adrs.append(i)
adrs.reverse()

def getMeet(adr,total,finishTime):
    global adrs
    try:
        start,end=adrs[adr],arr[adrs[adr]] 
    except:
        return total
    r2=getMeet(adr+1,total,finishTime)
    if finishTime<=start:
        r1=getMeet(adr+1,total+1,end)
        return max(r1,r2)
    return r2
print(getMeet(0,0,-1)+sameValue)