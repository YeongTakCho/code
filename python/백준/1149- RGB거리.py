import sys
read= sys.stdin.readline

def sol():
    N  = int(read())
    RGB = [list(map(int,read().split())) for _ in range(N)]
    
    for n in range(N-1):
        RGB[n+1][2] += RGB[n][0] if RGB[n][0] < RGB[n][1] else RGB[n][1]
        RGB[n+1][1] += RGB[n][0] if RGB[n][0] < RGB[n][2] else RGB[n][2]
        RGB[n+1][0] += RGB[n][1] if RGB[n][1] < RGB[n][2] else RGB[n][2]
    return min(RGB[N-1])

print(sol())