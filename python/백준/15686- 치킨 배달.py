import sys; read = sys.stdin.readline

N,M = map(int,read().strip().split())

town = [list(map(int,read().strip().split())) for _ in range(N)]
table = [[0] * N* 2 for _ in range(13)]
houses = []
chickens = []

for i in range(N):
    for j in range(N):

        if town[i][j] ==1:
            houses.append((i,j))
            for chicken_count in range(len(chickens)):
                dis =  (lambda p1, p2: abs(p1[0] -p2[0]) + abs(p1[1] - p2[1]))(chickens[chicken_count],(i,j))
                table[chicken_count][len(houses)-1] =dis
                
        if town[i][j] ==2:
            chickens.append((i,j))
            for houses_count in range(len(houses)):
                dis=(lambda p1, p2: abs(p1[0] -p2[0]) + abs(p1[1] - p2[1]))((i,j),houses[houses_count])
                table[len(chickens)-1][houses_count] =  dis
def backtracking(n,m):                
    def dfs(start,data):
        if len(stack)==m:
            data.append(stack.copy())
            return
        for i in range(start,n+1):
            stack.append(i-1)
            dfs(i+1,data)
            stack.pop()
    stack=[]
    data= []
    dfs(1,data)
    return data

backtracking_data = backtracking(len(chickens), M)

mini = 10**4
for combination in backtracking_data:
    result = 0
    
    for houses_count in range(len(houses)):
        minii = 10**3
        for c in combination:
            if table[c][houses_count] < minii:
                minii = table[c][houses_count]
        result += minii
    
    if result < mini:
        mini = result
        
print(mini)