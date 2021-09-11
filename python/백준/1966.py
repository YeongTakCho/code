test_case=int(input())
Ns=[]; Ms=[]; imps=[] #N: 문서의 갯수 M: 궁금한 문서의 위치 (start=0) imp(importance): N개의 문서의 중요도
for test in range(test_case):
    N, M=map(int,input().split())
    Ns.append(N);Ms.append(M)
    imps.append(list(map(int,input().split())))

def fbnp(nums): #find biggest num place
    biggest_num=0
    biggest_state=0
    now_state=0
    for num in nums:
        num=num[0]
        if num>biggest_num:
            biggest_num=num
            biggest_state=now_state
        now_state+=1
    return biggest_num, biggest_state

for test in range(test_case):

    N=Ns[test];M=Ms[test];imp=[]
    for i in imps[test]:
        imp.append([i,0])
    imp[M][1]=1
    seq=0

    while True:
        biggest_num, biggest_state=fbnp(imp)
        if biggest_state!=0:
            imp.append(imp.pop(0))
        else:
            seq+=1
            if imp[biggest_state][1]==1:
                break
            imp.pop(biggest_state)

    print(seq)


