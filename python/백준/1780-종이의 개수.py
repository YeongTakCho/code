import sys

def quardTree(x,y,Len):
    global nums, result
    color=nums[y][x]
    if Len=='1':
        result[int(color)+1]+=1
        return
    breakFor=False
    for _y in range(y,y+Len):
        for _x in range(x,x+Len):
            if nums[_y][_x] != color:
                breakFor=True
                break
        if breakFor==True:
            break
    if breakFor==False:
        result[int(color)+1]+=1
    else:
        nLen=Len//3
        for i in range(3):
            for j in range(3):
                quardTree(x+nLen * i,y+nLen* j , nLen)

        
result=[0,0,0]
read=sys.stdin.readline
N=int(read())
nums=list()
for _ in range(N):
    nums.append(read().split())
quardTree(0,0,N)
for _ in range(3):
    print(result[_])
#https://www.acmicpc.net/source/33652204