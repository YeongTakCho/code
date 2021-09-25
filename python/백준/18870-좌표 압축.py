import sys; input=sys.stdin.readline
N=int(input())
nums=list(map(int,input().split()))
numsDict=dict()
i=0
for key in sorted(list(set(nums))):
    numsDict[key]=i
    i+=1
for num in nums:
    print(numsDict[num],end=' ')
print()
