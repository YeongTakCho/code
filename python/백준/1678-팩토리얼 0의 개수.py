n=int(input())
two=0
five=0
for i in range(2,n+1,2):
    num=i
    while num%2==0:
        num/=2
        two+=1
for i in range(5,n+1,5):
    num=i
    while num%5==0:
        num/=5
        five+=1
print(min(two,five))