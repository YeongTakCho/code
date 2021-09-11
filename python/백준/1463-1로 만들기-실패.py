n=int(input())

def rest23(num):
    return [num%2, num%3]

def toOne(num,totalMove):
    case1=[[0,0],[1,0],[1,1]]
    case2=[[0,2]]
    case3=[[0,1],[1,2]]
    if num==1:
        return totalMove
    rest=rest23(num)

    if rest in case1:
        totalMove+=(rest[1]+1)
        return toOne(int(num/3),totalMove)

    elif rest in case2:
        totalMove+=(rest[0]+1)        
        return toOne(int(num/2),totalMove)

    elif rest in case3:
        moves1=toOne(int(num/3),totalMove+(rest[1]+1))
        moves2=toOne(int(num/2),totalMove+(rest[0]+1))
        if moves1>moves2:
            return moves2
        else:
            return moves1
print(toOne(n,0))

