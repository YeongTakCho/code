n=int(input())
tests=[]
for i in range(n):
    tests.append(int(input()))
list1=[1,1,1,2,2]
for num in tests:
    try:
        print(list1[num-1])
    except:
        for i in range(len(list1),num):
            list1.append(list1[i-1]+list1[i-5])
        print(list1[num-1])    