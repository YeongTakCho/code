n=int(input())
nstr=['I']
for i in range(n):
    nstr.append('O')
    nstr.append('I')
nstr=''.join(nstr)
m=int(input())
S=input()

count=0
for pos in range(m-n*2):
    pstr=S[pos:pos+n*2+1]
    if pstr==nstr:
        count+=1
print(count)
