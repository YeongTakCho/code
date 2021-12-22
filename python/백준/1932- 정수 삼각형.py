import sys
read = sys.stdin.readline

def sol():
    N= int(read())
    triangle = [list(map(int,read().split())) for _ in range(N)]
    
    for n in range(N-2,-1,-1):
        for index in range(n+1):
            triangle[n][index] += max([triangle[n+1][index], triangle[n+1][index+1]])
            
    return triangle[0][0]
print(sol())