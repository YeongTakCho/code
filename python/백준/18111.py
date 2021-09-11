n,m,b=map(int,input().split())
sums=b
d=dict()
for _ in range(n):
   for num in (list(map(int,input().split()))):
      if num not in d:
         d[num]=1
      else:
         d[num]+=1
for key in list(d):
   sums+=key*d[key]

maxFloor=int(sums/(n*m))
if maxFloor>256:
       maxFloor=256

def getTime(d,floor):
   sumTime=0
   for key in list(d):
      amount=d[key]
      dist=key-floor #양수면 *2 음수면*1
      if dist>0:
         sumTime+=dist*2*amount
      else:
         sumTime-=dist*amount
   return sumTime

lowestTime=getTime(d,0)
lowestTimeFloor=0


for floor in range(1,maxFloor+1):
   nTime=getTime(d,floor)
   if nTime<=lowestTime:
      lowestTime=nTime
      lowestTimeFloor=floor

print(lowestTime,lowestTimeFloor)
