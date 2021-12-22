import sys
import copy

read = sys. stdin. readline

def sol(): #sqread active 미완
    
    def spread():
        chagne = copy.deepcopy(clean_room)
        for i in range(R):
            for j in range(C):
                if not room[i][j]==0:
                    fifth = room[i][j] //5
                    if (i==0 or i ==R-1) or (j==0 or j ==C-1):# is edge
                        if (i==0 or i ==R-1) and (j==0 or j ==C-1): # is vertex (remain 3/5)
                            if i==0:
                                room[i+1][j] += fifth
                            else:
                                room[i-1][j] += fifth
                            
                            if j==0:
                                room[i][j+1] +=fifth
                            else:
                                room[i][j-1] += fifth
                            room[i][j] -= fifth*2
                            
                        else: # edge but not vertex (remain 2/5)
                            pass
                    else: #not edge (remain 1/5)
                        pass
                            
    def active():
        pass
    
    def run(n):
        for _ in range(n):
            spread()
            active()
    
    R,C,T  = map(int,read().split())
    room = [list(map(int,read().split())) for _ in range(R)]
    clean_room = [[0] * C] * R
    dust=  0
        
    for i in range(R):
        if room[i][0] == -1:
            machine = i
            break
    
    run(T)
    
    for i in range(R):
        dust+= sum(room[i])
        
    return dust
print(sol())