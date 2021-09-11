p_nums1=list([2])

for x in range(3,1000,2):
    key=0
    for d_num in p_nums1:
        if d_num> x**0.5:
            break
        if x%d_num ==0:
            key=1
            break
    if key ==0:
        p_nums1.append(x)
p_nums1=set(p_nums1)
input()
nums=map(int,input().split())
count=0
for num in nums:
    if num in p_nums1:
        count+=1
print(count)
