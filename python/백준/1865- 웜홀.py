import sys; read= sys.stdin.readline
from collections import deque

result_arr = []
for cnttc in range(int(read())):
    N, nM, nW = map(int,read().strip().split())
    rSet = [set() for _ in range(N)]
    r= [[None]*N for _ in range(N)]
    T = [False] * N
    
    for _ in range(nM):
        s, e, t = map(int,read().strip().split())
        s, e= s-1, e-1
        if r[s][e] == None:
            rSet[s].add(e)
            r[s][e] = t
        elif t < r[s][e]:
            r[s][e]= t
    
    for _ in range(nW):
        s, e, t = map(int,read().strip().split())
        s, e, t= s-1, e-1, -t
        if r[s][e] == None:
            rSet[s].add(e)
            r[s][e] = t
        elif t < r[s][e]:
            r[s][e]= t
    
    result ='No'
    for s in range(N):
        if T[s] == False:
            T[s] = 0
            q= deque()
            for e in rSet[s]:
                q.append([e,r[s][e]])
                
            while q:
                n_s, t = q.popleft()
                if T[n_s]:
                    if t< T[n_s]:
                        result = 'Yes'
                        break
                    
                
                elif T[n_s] == False:
                    T[n_s] = t
                    for e in rSet[n_s]:
                        q.append([e, t + r[n_s][e]])
                              
            if result == 'Yes':
                break
    result_arr.append(result)

for result in result_arr:
    print(result)    
    
            
                