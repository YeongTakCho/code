import sys
n=int(input())
setList=[];schedules=[]
totalScheduel=0
highest_total=0
for i in range(n):
    n1,n2=(map(int,sys.stdin.readline().strip().split()))
    if n1==n2:
        totalScheduel+=1
    else:
        setP=(set(n+0.5 for n in range(n1,n2)))
        key=0
        for set1 in setList: #더 큰 집합을 제거
            if set1.issubset(setP):
                key=1
                break
            if setP.issubset(set1):
                setList.remove(setP)
        if key==0:
            setList.append(setP)
lenList=len(setList)
def getSchedue(setListIndex,setSchedue,totals):
    global setList,lenList,highest_total
    setP=setList[setListIndex]
    setListIndex+=1
    if setListIndex!=lenList:
        if setP.isdisjoint(setSchedue):
            getSchedue(setListIndex,setSchedue|setP,totals+1)
        getSchedue(setListIndex,setSchedue,totals)
    else:
        if setP.isdisjoint(setSchedue):
            totals+=1
        if totals>highest_total:
            highest_total=totals

getSchedue(0,set(),totalScheduel)
print(highest_total)