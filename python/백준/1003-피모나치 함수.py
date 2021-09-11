testcase=int(input())
testNums=[]
dp=[[1,0],[0,1]]
for i in range(testcase):
    testNums.append(int(input()))
maxNum=max(testNums)
for i in range(2,maxNum+1):
    num0=dp[i-2][0]+dp[i-1][0]
    num1=dp[i-2][1]+dp[i-1][1]
    dp.append([num0,num1])
for num in testNums:
    print("%d %d"%(dp[num][0],dp[num][1]))
