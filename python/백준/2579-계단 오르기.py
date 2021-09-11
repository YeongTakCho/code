global n
n=int(input())
stairs=[int(input()) for _ in range(n)]
stairs.reverse()
check=[0 for _ in range(n)]
check[0]=1
def def1(p2,p1,state,list1): #state start from 0
    if state==n:
        sum=0
        for i in range(n):
            sum+=check[i]*stairs[i]
        return sum
    if p2==1 and p1==1:
        list1[state]=0
        return def1(1,0,state+1,list1)
    else:
        max=0
        for i in range(2):
            list1[state]=i
            _return=def1(p1,i,state+1,list1)
            if _return>max:
                max=_return
        return max
print(def1(0,1,1,check))