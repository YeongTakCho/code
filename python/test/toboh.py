import sys
nums=list(map(int,sys.stdin.readline().split()))
nums.sort()
mylist=[0]*max(nums)
for i in nums:
    mylist[i-1]+=1
if len(nums)%2==1:
    middle=nums[len(nums)//2]
else:
    middle=(nums[len(nums)//2]+nums[len(nums)//2-1])/2
print('len=',end='');print(len(nums))
print('middle=',end='');print(middle)
print('avarge=',end='');print(sum(nums)/len(nums))
print(list(enumerate(mylist,1)))
print(nums[8],nums[23],nums[6],nums[24])