def num(m,n,x,y):
    while x<=m*n:
        if x%n==y: #n==y일경우 포함 x
            return x
        x+=m
    return -1

testcase=int(input())
for i in range(testcase):
    m,n,x,y=map(int,input().split())
    print(num(m,n,x,y))

# from sys import stdin

# # first-class func
# rd = stdin.readline

# def get_gcd(n1, n2):
#     while n1 % n2:
#         tmp = n1
#         n1 = n2
#         n2 = tmp % n2
    
#     return n2


# def get_lcm(n1, n2):
#     gcd = get_gcd(n1, n2)
#     last_year = n1*n2//gcd

#     return last_year

# def get_inca_year(M, N, x, y):
#     last_year = get_lcm(M,N)
#     y = 0 if y == N else y
    
#     for year in range(x,last_year+1,M):
#         if year % N == y:
#             return year

#     return -1


# if __name__ == "__main__":
#     T = int(rd())

#     for _ in range(T):
#         M, N, x, y = map(int, rd().split())
#         if M > N:
#             M, N = N, M
#             x, y = y, x

#         ans = get_inca_year(M, N, x, y)
#         print(ans)