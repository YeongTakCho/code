kn=input()
k,n=kn.split(); k=int(k); n=int(n)
lines_len=[]
for i in range(k):
    lines_len.append(int(input()))

max_len=1
while True:
    sum_lines=0
    for i in range(k):
        sum_lines+=lines_len[i]//(max_len*2)
    if sum_lines>=n:
        max_len*=2
    else:
        break
sum_num=max_len/2

while sum_num>=1:
    sum_lines=0
    for i in range(k):
        sum_lines+=lines_len[i]//(max_len+sum_num)
    if sum_lines>=n:
        max_len+=sum_num
    sum_num//=2
print(int(max_len))