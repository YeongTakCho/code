import sys
read = sys. stdin. readline

Testcase=int(read())
result=list()

for t in range(Testcase):
    n = int(read())
    clothes_dict=dict()

    for _ in range(n):

        inV= read().split()

        try:
            clothes_dict[inV[1]]+=1
        except:
            clothes_dict[inV[1]]=1

    clothes= [ clothes_dict[key] for key in  clothes_dict.keys()]

    total=1

    for v in clothes:
        total*= v+1
    result.append(total-1)

for v in result:
    print(v)