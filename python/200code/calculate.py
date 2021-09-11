n1= int(input('input num1 '))
n2= int(input('input num2 '))

print(n1, n2)
n12= n1%n2
print('n1 mod n2 is %d' %n12)

ret1, ret2= divmod(n1,n2)
print('ret1 red2 in divmod n1 n2 is %d %d'%(ret1,ret2))

h1=hex(n1); h2=hex(n2)
print(h1+h2)

