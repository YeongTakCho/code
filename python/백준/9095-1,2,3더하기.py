import sys; input=sys.stdin.readline
from math import factorial

T=int(input().strip())
nums=[int(input().strip()) for _ in range(T)]
for num in nums:
    total=0
    for i in range(num//3+1):
        _num=num-i*3
        for j in range(_num//2+1):
            remain=_num-j*2
            devide1=factorial(i) if  i!=0 else 1
            devide2=factorial(j) if j!=0 else 1
            devide3=factorial(remain) if remain !=0 else 1
            total+=factorial(i+j+remain)//(devide1*devide2*devide3)
    print(total)