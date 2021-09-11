# 왼쪽 위가 흰색일 경우와 검은색일 경우에 바뀌는 칸을 표시, 8*8칸 안에 표시 된 칸의 갯수의 최솟값을 구함.
#10->세로->row, 13=가로=col
#왼쪽 위가 흰색일 경우와 검은 색일 경우는 따로 구할 필요가 없다.
#흰색일때 케이스를 w, 검은색일때 케이스를 b라고 한다면 w+b=64로 보존된다.
#바뀌는 갯수의 최솟값은 32를 넘을 수 없음 (왼쪽위가 흰색일 때 바뀌어야 하는 갯수가 33개라면 검은색 일 때 31개이다.)

rowcol=input()
row,col=rowcol.split();row=int(row);col=int(col)
#흰색 1, 검은색 0
#바뀌는 부분 1, 안바뀌는 부분0
array = [[0 for col in range(col)] for row in range(row)] #원형
array_b = [[0 for col in range(col)] for row in range(row)] #왼쪽위가 검은색 =>가로 + 세로 = 홀수 -> 흰색

for i in range(row):
    color=input()
    j=0
    for each_color in color:
        if each_color=='W':
            array[i][j]=1
        j+=1
for i in range(row):
    for j in range(col):
        if (i+j)%2!=array[i][j]:
            array_b[i][j]=1

def wbcase(n):
    if n<=32:
        return n
    else:
        return 64-n
smallest=32
for i in range(row-7):
    for j in range(col-7):
        sum=0
        for i1 in range(8):
            for j1 in range(8):
                sum+=array_b[i+i1][j+j1]
        sum=wbcase(sum)
        if sum<smallest:
            smallest=sum
print(smallest)



