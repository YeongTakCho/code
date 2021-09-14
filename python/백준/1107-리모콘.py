import sys,math
dest=int(sys.stdin.readline())
errbuttonN=int(sys.stdin.readline())
errbutton=list(map(int,sys.stdin.readline().split()))
enablebutton=[0,1,2,3,4,5,6,7,8,9]
moving=0

for i in errbutton:
    enablebutton.remove(i)

def canGoChannel(n):
    global enablebutton
    for i in str(n):
        if int(i) not in enablebutton:
            return 1
    return 0

if canGoChannel(dest)==1:
    channels=[dest-1,dest+1]
    moving+=1
    while True:
        if canGoChannel( channels[0]) ==0:
            moving+=(int(math.log10(channels[0]))+1)
            break
        elif canGoChannel( channels[1]) ==0:
            moving+=(int(math.log10(channels[1]))+1)
            break
        if channels[0]!=0:
            channels[0]=channels[0]-1
        channels[1]=channels[1]+1
        moving+=1
if moving > abs(dest-100):
    moving=abs(dest-100)
print(moving)