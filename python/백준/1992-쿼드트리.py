import sys

def quardTree(x,y,Len):
    global nums, result
    color=nums[y][x]
    if Len=='1':
        result.append(color)
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
        result.append(color)
    else:
        result.append('(')
        quardTree(x,y,Len//2)
        quardTree(x+Len//2,y,Len//2)
        quardTree(x,y+Len//2,Len//2)
        quardTree(x+Len//2,y+Len//2,Len//2)
        result.append(')')

        
result=list()
read=sys.stdin.readline
N=int(read())
nums=list()
for _ in range(N):
    nums.append(read().rstrip())
quardTree(0,0,N)
print(''.join(result))
