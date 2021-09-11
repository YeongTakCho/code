import sys
paper=[];white=0;black=0

n=int(input())
for i in range(n):
    paper.append(list(map(int,sys.stdin.readline().strip().split())))

def checkColor(xState,yState,squareLen):
    global paper
    color=paper[yState][xState]
    key=0
    for y in range(yState,yState+squareLen):
        for x in range(xState,xState+squareLen):
            colorN=paper[y][x]
            if colorN != color:
                key=1
                break
        if key==1:
            break
    if key==1:
        return 2 #같지 않음
    elif key==0:
        return color #모두 같으면 색을 반환

def checkSquare(xState,yState,squareLen):
    global white,black
    result=checkColor(xState,yState,squareLen)
    if result ==2:
        squareLen= squareLen//2
        checkSquare(xState,yState,squareLen)
        checkSquare(xState,yState+squareLen,squareLen)
        checkSquare(xState+squareLen,yState,squareLen)
        checkSquare(xState+squareLen,yState+squareLen,squareLen)
    elif result==1:
        black+=1
    elif result==0:
        white+=1
checkSquare(0,0,n)
print(white)
print(black)

