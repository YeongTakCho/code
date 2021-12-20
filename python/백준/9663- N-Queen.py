

def queen (data, vertical, diagonal_plus, diagonal_minus,i, N): #n = the state data manipulated
    if i==N:
        return 1
    
    val= 0
    for j in range(N):
        if vertical[j]:
            if diagonal_plus[i+j]:
                if diagonal_minus[i-j+N-1]:
                    
                    _data = data[:]; _data[i] = j
                    _vertical = vertical[:]; _vertical[j] = False
                    _diagonal_plus = diagonal_plus[:]; _diagonal_plus[i+j] = False
                    _diagonal_minus = diagonal_minus[:]; _diagonal_minus[i-j+N-1] = False
                    
                    val+= queen(_data, _vertical, _diagonal_plus, _diagonal_minus, i+1, N)
    return val
for N in range(1,16):
    print('%d. %d' %(N, queen([None]*N,[True]*N, [True]*(N*2-1),[True]*(N*2-1), 0, N)))
    