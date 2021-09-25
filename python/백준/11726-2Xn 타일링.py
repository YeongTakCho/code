def factorial(k):
    fact = 1
    for i in range(1, k+1):
        fact *= i
    return fact

def nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r))

n=int(input())

def ncr(n):
    
    if n==1:
        return 1
    else:
        R=1
        total=1
        n=n-1
        while True:
            total+=nCr(n,R)
            n-=1
            R+=1
            if n<R:
                break
        return total

print(int((ncr(n))%10007))
    

