N, M = map(int,input().strip().split())
trees = list(map(int,input().strip().split()))
trees.sort(reverse= True) #n log n
trees.append(0)

s=0

for cnt in range(1,N+1): # n
    l = trees[cnt]
    s += (trees[cnt-1] - trees[cnt]) * cnt
    
    if s>=M:
        min_l = trees[cnt]
        break
    
# if l +=1 -> s  -= cnt
result  = min_l+ (s-M) //cnt
print(result)