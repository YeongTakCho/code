import sys; read= sys.stdin.readline

n = int(read())
seq = [int(read()) for _ in range(n)]
cal = []; p = '+'; m = '-'
arr = []; arr_cnt = 1
for v in seq:
    while v>= arr_cnt:
        arr.append(arr_cnt)
        arr_cnt+=1
        cal.append(p)
        
    if v< arr_cnt:
        if v == arr.pop():
            cal.append(m)
        else:
            cal = ['NO']
            break
        
for c in cal:
    print(c)