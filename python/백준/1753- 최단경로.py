#시간초과
import sys
read= sys.stdin.readline

def sol(): #Dijkstra algorithm
    Vn, En = map(int,read().split())
    S= [int(read()) -1] #starts
    D= ['INF' for _ in range(Vn)]; D[S[0]] = 0 #shortest way value (can be changed in progress)
    C= [dict() for _ in range(Vn)] #line
    V= [False for _ in range(Vn)]; V[S[0]] = True #V[i] = D[i] is shortest (D[i] is not changed anymore)
    
    #input lines
    for _ in range(En):
        u, v, w= map(int,read().split())    
        if v-1 in C[u-1]:
            C[u-1][v-1]= min(C[u-1][v-1], w)
        else:
            C[u-1][v-1]= w
            
    def dijkstra():
        while False in V:
            u= None; v= None
            minC = 11
            remove=[]
            
            for s in S:
                for key, value in C[s].items():
                    if V[key]:
                        remove.append([s,key])
                        continue
                    
                    if value<minC:
                        minC = value
                        u = s; v = key
                        
            if minC == 11:
                break
            
            for data in remove:
                del C[data[0]][data[1]]
                
            S.append(v)
            D[v] = D[u] + minC
            V[v] = True
            del C[u][v]
            
            for key, value in C[v].items():
                if D[key] == 'INF':
                    D[key] = D[v] + value
                else:
                    D[key] = min(D[key], D[v]+ value)
    dijkstra()
    return D
    
r = sol()
for v in r:
    print(v)