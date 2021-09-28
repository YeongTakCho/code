import sys

def quardTree(x,y,Len):
    global nums
    color=nums[y][x]
    if Len=='1':
        return 
        # 
    for _y in range(y,y+Len):
        for _x in range(x,x+Len):
            if nums[_y][_x] == color:
                continue
            else:
                pass
                # 

read=sys.stdin.readline
N=int(read())
nums=list()
for _ in range(N):
    nums.append(read().rstrip())
