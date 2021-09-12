import sys
testsNum=int(input())
commandss=[];commandsLens=[];numss=[]
for i in range(testsNum):
    commandss.append(sys.stdin.readline().strip())
    commandsLens.append(int(sys.stdin.readline().strip()))
    numsP=sys.stdin.readline().strip();numsP=numsP.replace('[','');numsP=numsP.replace(']','')
    try:
        numss.append(list(map(int,numsP.split(','))))
    except:
        numss.append(list())

for test in range(testsNum):
    reverse=0
    commands=commandss[test]
    commandsLen=commandsLens[test]
    nums=numss[test]
    key=0
    for command in commands:
        if command=='R':
            if reverse==1:
                reverse=0
            elif reverse==0:
                reverse=1
        elif command=='D':
            try:
                if reverse==0:
                    nums.pop(0)
                elif reverse==1:
                    nums.pop()
            except:
                print('error')
                key=1
                break
    if reverse==1:
        nums.reverse()
    if key==1:
        continue
    elif key==0:
        print(nums)
            
