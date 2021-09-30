import sys

def sol():
    read=sys.stdin.readline
    N=int(read())
    nums=[list(map(int,read().split())) for _ in range(N)]
    result=[0,0,0]
    recursive(nums,0,0,N,result)
    print(result[-1])
    print(result[0])
    print(result[1])

def recursive(nums,x,y,Len,result):
    color=nums[y][x]
    if Len==1:
        result[color]+=1
        return
    else:
        if is_same_color(nums,x,y,Len):
            result[color]+=1
        else:
            nLen=Len//3
            for i in range(3):
                for j in range(3):
                    recursive(nums,x+nLen*i,y+nLen*j,nLen,result)

def is_same_color(nums,x,y,Len):
    color=nums[y][x]
    for _x in range(x,x+Len):
        for _y in range(y,y+Len):
            if nums[_y][_x] != color:
                return False
    return True

sol()