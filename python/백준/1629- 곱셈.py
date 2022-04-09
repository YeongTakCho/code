import math
A, B, C = map(int,input().strip().split())
MAX= math.floor(math.log2(B))
mod_arr = [0] * (MAX+1)
mod_arr[0] = A % C
n=1

for cnt in range(1,MAX+1):
    mod_arr[cnt] = (mod_arr[cnt-1] ** 2) % C

while B >0: 
    power = math.floor(math.log2(B))
    B = B - 2 ** power
    n = (n * mod_arr[power]) % C
print(n)