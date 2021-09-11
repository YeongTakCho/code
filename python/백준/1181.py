n=int(input())
strs=[]
for i in range(n):
    strs.insert(i,input())
strs.sort()
strs.sort(key=len)
result=[strs[0]]
i=0
for value in strs:
    if value != result[i]:
        result.append(value)
        i+=1
for i in range(len(result)):
    print(result[i])
