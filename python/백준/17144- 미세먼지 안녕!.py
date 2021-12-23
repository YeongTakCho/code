import sys
import copy

read = sys. stdin. readline

def sol(): #sqread active 미완
    R,C,T  = map(int,read().split())
    room = [list(map(int,read().split())) for _ in range(R)]
    clean_room = [[0] * C for _ in range(R)]
    dust=  0
    
    for i in range(R):
        if room[i][0] == -1:
            machine = [i]
            break
        
    def spread():

        change = copy.deepcopy(clean_room)
        for i in range(R):
            for j in range(C):
                if not (room[i][j]==0 or room[i][j] ==-1):
                    fifth = room[i][j] //5
                    if not(i==0 or (i== machine[0]+2 and j==0)): #upside
                        change[i-1][j] += fifth
                        change[i][j] -=fifth
                    if not(i == R-1 or (i==machine[0]-1 and j==0)): #downside
                        change[i+1][j] +=fifth
                        change[i][j] -=fifth
                    if not(j ==0 or ((i==machine[0] or i ==machine[0]+1) and j==1)): #leftside
                        change[i][j-1] += fifth
                        change[i][j] -=fifth
                    if not(j== C-1):
                        change[i][j+1] += fifth
                        change[i][j] -=fifth
        
        for i in range(R):
            for j in range(C):
                room[i][j] += change[i][j]
                                            
    def active():
        for i in range(machine[0]-1,-1,-1):
            room[i+1][0] = room[i][0]
        for i in range(machine[0]+2,R):
            room[i-1][0] = room[i][0]
            
        for j in range(1, C):
            room[0][j-1] = room[0][j]
            room[R-1][j-1] = room[R-1][j]
            
        for i in range(1,machine[0]+1):
            room[i-1][C-1] = room[i][C-1]
        for i in range(R-2, machine[0], -1):
            room[i+1][C-1] = room[i][C-1]
            
        for j in range(C-2,0,-1):
            room[machine[0]][j+1] = room[machine[0]][j]
            room[machine[0]+1][j+1] = room[machine[0]+1][j]
        
        room[machine[0]][1] =0
        room[machine[0]+1][1] =0
        room[machine[0]][0] = -1
        room[machine[0]+1][0] = -1
        
    def run(n):
        for _ in range(n):
            spread()
            active()
    run(T)
    
    for i in range(R):
        dust+= sum(room[i])
    
    dust +=2 #공기청정기 값 제거
    return dust

print(sol())