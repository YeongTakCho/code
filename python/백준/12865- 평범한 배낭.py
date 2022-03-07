import sys; read= sys.stdin.readline

N,K = map(int,read().strip().split())
s= [list(map(int,read().strip().split())) for _ in range(N)]
s.sort(key= lambda d: (d[0],-d[1]))

def getMAX(cnt,v,rest):
    max = v
    while cnt < len(s):
        if s[cnt][0] > rest:
            return max
        
        else:
            val = getMAX(cnt+1, v+ s[cnt][1], rest - s[cnt][0])
            if val > max:
                max =val
            cnt+=1
    return max

print(getMAX(0,0,K))
    