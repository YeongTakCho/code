#https://www.acmicpc.net/source/5298361
n=int(input())

board = []
for  i in range(n):
    board.append(list(map(int,input())))

def infect(board: list,i : int ,j : int) -> int:
    if not ( 0<=i<len(board) and 0<=j<len(board)):
        return 0

    if board[i][j]==0:
        return 0

    board[i][j]=0
    res =1
    for newi,newj in ((i-1,j),(i+1,j),(i,j+1),(i,j-1)):
        res+=infect(board,newi,newj)         # board는 call by reference이기 때문에 중복되서 세어지지 않는다.

    return res

total=0
sizes= []

for i in range(len(board)):
    for j in range(len(board[0])):
        town = infect(board,i,j)
        if town !=0:
            total+=1
            sizes.append(town)

print(total)

sizes.sort()
for size in sizes:
    print(size)

