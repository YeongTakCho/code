import sys
import copy

read = sys. stdin. readline
virus = list()
lab = list()


N, M = map(int, input().split())

for _ in range(N):
    lab.append(list(map(int,input().split())))

    

for n in range(N):
    for m in range(M):
        if lab[n][m] ==2:
            virus.append((n,m))

def lab_test(lab,N,M,virus):
    result = 0

    while virus:
        new_virus = list()

        for each_virus in virus:
            n, m = each_virus

            if n != 0 :
                if lab[n-1][m] ==0:
                    lab[n-1][m] =2
                    new_virus.append((n-1,m))

            if n != N-1:
                if lab[n+1][m] ==0:
                    lab[n+1][m] =2
                    new_virus.append((n+1,m))

            if m !=0:
                if lab[n][m-1] ==0:
                    lab[n][m-1] =2
                    new_virus.append((n,m-1))

            if m != M-1:
                if lab[n][m+1] ==0:
                    lab[n][m+1] =2
                    new_virus.append((n,m+1))

        virus=new_virus


    for n in range(N):
        for m in range(M):
            if lab[n][m] ==0:
                result+=1

    return result
 
def make_wall(lab, start, walls, N,M,virus):

    if len(walls) ==3:
        new_lab=  copy.deepcopy(lab)
        for wall in walls:
            new_lab[wall[0]][wall[1]] = 1
        return lab_test(new_lab,N,M,copy.deepcopy(virus))
    
    biggest =0
    n , m =start

    for _m in range(m+1, M):
        if lab[n][_m] ==0:
            value =make_wall(lab,(n,_m), walls + [(n,_m)], N, M, virus)
            if value > biggest:
                biggest= value

    for _n in range(n+1,N):
        for _m in range(M):
            if lab[_n][_m] ==0:
                value = make_wall(lab,(_n,_m),walls + [(_n,_m)], N, M, virus)
                if value > biggest:
                    biggest= value
    return biggest

value = make_wall(lab,(0,0),list(), N,M,virus)
print(value)