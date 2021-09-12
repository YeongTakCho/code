def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a
print(6*9//gcd(6,9))