n=int(input())
m=int(input())
S=input()
count=0

past=0 #0(O)or1(I)
persist=0
persistLen=int()
for s in S:
    if s=='I':
        if persist==0:
            persist=1
            persistLen=0
        elif persist==1:
            if past==0:
                persistLen+=1
            elif past==1:
                if persistLen>=n:
                    count+=(persistLen-n+1)
                persistLen=0
        past=1
    elif s=='O':
        if persist==0:
            pass
        elif persist==1:
            if past==1:
                pass
            elif past==0:
                if persistLen>=n:
                    count+=(persistLen-n+1)
                persist=0
                persistLen=0
        past=0
if persistLen>=n:
    count+=(persistLen-n+1)
print(count)

