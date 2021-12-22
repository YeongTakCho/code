#참고: https://goplanit.site/46.%20Algorithm(9663_py)/
def queen(n,N):
    global result
    if n==N:
        result +=1
        return
    else:
        for i in range(N):
            row[n] =i
            key= True
            for j in range(n):
                if row[j] == row[n] or (row[n]-n) == (row[j] - j) or (row[n] +n) == (row[j]+j):
                    key= False
                    break
            if key:
                queen(n+1,N)
        
s = int(input())
result = 0
row = [300] * s
queen(0, s)

print(result)