from datetime import datetime
start=datetime.now()
m,n=input().split();m=int(m);n=int(n)
p_nums1=list([2])
p_nums2=list([2])
if m<=2:
    print(2)
for x in range(3,n+1,2):
    key=0
    for d_num in p_nums1:
        if d_num> x**0.5:
            break
        if x%d_num ==0:
            key=1
            break
    if key ==0:
        p_nums1.append(x)
        if x>=m:
            print(x)
end=datetime.now()
print('datetime.now() type is %s'%type(start))
elapsed=end-start
print('총 계산 시간:',end='');print(elapsed)
elapsed_ms=int(elapsed.total_seconds()*1000)
print('총 계산 시간:%dms'%elapsed_ms)
