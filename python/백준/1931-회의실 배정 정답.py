import sys
input=sys.stdin.readline

N=int(input())
arr=sorted([tuple(map(int,input().split())) for _ in range(N)],key=lambda x: (x[1],x[0]))
end=0
total=0
for x in arr:
    if x[0]>=end:
        end=x[1]
        total+=1
print(total)