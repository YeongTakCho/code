#n번 반복(1~n까지 삽입하는 것을 반복)=> 1 삽입, nums[0]을 만들 수 있는지 확인, 가능하면 추출 후 nums[1]을 만들 수 있는지 확인, 불가능하면 2삽입
n=int(input())
nums=[]
for i in range(n):
    nums.append(int(input()))
stack=[] #last in first out
stack_len=0

search_state=0
search_num=nums[search_state]

pmlist=[]

for i in range(1,n+1):
    if i==search_num:
        search_state+=1
        search_num=nums[search_state]
        key=1
        pmlist.append('+')
        pmlist.append('-')
        while key:
            if stack_len==0:
                key=0
                continue
            else:
                last_num=stack[stack_len-1]
                if last_num==search_num:
                    search_state+=1
                    if search_state !=n:
                        search_num=nums[search_state]
                    stack.pop()
                    stack_len-=1
                    pmlist.append('-')
                else:
                    key=0
    else:
        stack.append(i)
        stack_len+=1
        pmlist.append('+')
if stack==[]:
    for result in pmlist:
        print(result)
else:
    print('NO')