N=int(input())
A=[]
A=sorted(list(set(input().split())))
N=len(A)
M=int(input())
B=input().split()

for the_num in B:
    plus_num=1
    search_state=0
    search_num=A[search_state]

    if search_num == the_num:
        print('1')

        continue
    key=1
    result_key=0
    for x in range(2):
        while result_key==0 and key==1 and plus_num==int(plus_num):
            plus_num=int(plus_num);search_state=int(search_state)
            if search_state + plus_num<N and A[search_state+plus_num]<=the_num:
                search_state+=plus_num
                search_num=A[search_state]
                if search_num==the_num:
                    result_key=1
                if x==0:
                    plus_num*=2
                else:
                    plus_num/=2
            elif x==0:
                plus_num/=2
                key=0
            else:
                plus_num/=2
        key=1
    if result_key==1:
        print(1)
    else:
        print(0)
