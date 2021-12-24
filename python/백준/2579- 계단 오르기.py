#시간초과
import sys
read = sys.stdin.readline

def sol():
    N= int(read())
    stair = [int(read()) for _ in range(N)]
    
    if N==1:
        return stair[0]
    
    stair.reverse()
    cumulation = [[0,0] for _ in range(N)] #[n1,n2] => n1: do not one steped n2: do one step 
    
    cumulation[0][0] = stair[0]; cumulation[0][1] = stair[0]
    cumulation[1][0] = 0; cumulation[1][1] = stair[1] + stair[0]
    
    for i in range(2,N):
        cumulation[i][0]+= stair[i]
        cumulation[i][0]+= max(cumulation[i-2][0],cumulation[i-2][1])
        cumulation[i][1]+= stair[i]
        cumulation[i][1]+= cumulation[i-1][0]

    return max(cumulation[N-2][1], cumulation[N-1][0], cumulation[N-1][1])
print(sol())