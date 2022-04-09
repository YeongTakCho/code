import sys; read= sys.stdin.readline
from collections import deque

result = []
for _ in range(int(read())):
    A, B = map(int,read().strip().split())
    q = deque([[A,str()]])
    v= set(); v.add(A)
    
    while q:
        n, r= q.popleft()
        if n == B:
            result.append(r)
            q.clear()
            
        else:
            tmp =n*2 % 10000
            if tmp not in v:
                v.add(tmp)
                q.append([tmp, r+ 'D'])
            tmp =n -1 if n >0 else 9999
            if tmp not in v:
                v.add(tmp)
                q.append([tmp, r+ 'S'])
            tmp =n % 1000 * 10 + n // 1000
            if tmp not in v:
                v.add(tmp)
                q.append([tmp, r+ 'L'])
            tmp =n % 10 * 1000 + n // 10
            if tmp not in v:
                v.add(tmp)
                q.append([tmp, r+ 'R'])

for v in result:
    print(v)