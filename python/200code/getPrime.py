def getPrime(x):
    if x%2==0:
        return 34
    else:
        for i in range(3,x//2,2):
            if x%i ==0:
                return 
        return x
list1=[4,123,1523,11113,11119]



list2=filter(getPrime,list1)
print(list(list2))
