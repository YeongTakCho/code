
multiline='''
life is too short
You need python
'''
print(multiline)
multiline="""
life is very short
You also need python\r why r is\'nt work
but I nedd \\r
\a
\000
\t \\t
"""
print(multiline)

head= 'python'
tail = ' is second'
print(head+tail)

print(head*2)

print('*'*50)
print('my program')
print('*'*50)

a= 'I will use len(a) and wonder how long it is'
print(len(a))
print(len('*'*50))
print(a[0])
print(a[-1])
b=a[0]+a[1]+a[2]+a[3]+a[4]
print(b)
b=a[0:4]
print(b)
print(a[6:])
print(a[-5:-1])
print(a[3:-5])
a='20210803sunny'
data=a[:8]
weather=a[8:]
print(data)
print(weather)

a= 'pithon'
print(a)
print(a[1])
#a[1]='y'
a= a[:1]+'y'+a[2:]
print(a)

print("I eat %d apples" %3)
print("I eat %s apples"%'many')
num=4
print('I eat %d apples'%num)
strs= 'much'
print("I eat %s apples"%strs)
print(" I eat %d and %s apples"%(num,strs))
num= 123456789.0123456789
print("%1.4f"%num)
num=10
day='three'
print("I eat {0}apples in {1}days {0}".format(num,day))
print("I eat {number} apples in {day} days".format(number=num,day=day))
print("{0:>10},wow".format("hi"))

print("{0:!^10}".format("hi"))
print("{0:?<10},wow".format("hi"))
print("{0:3<10},wow".format("hi"))
print("{{print{{}}}}".format())

d={'name':'hong', 'age':20}
print(f'my name is {d["name"]} and my age will be {d["age"]+1} in next year')

a= 'hobby'
print(a.count('b'))

a= 'python is the best choice'
a.find('k')
a.find('b')

print(','.join('abcd'))
print(','.join(['a','b','c','d']))

a='go to upPER'
print(a.upper())
b='GO TO loWER'
print(b.lower())
a_strip='   a    '
b_strip='   b    '
print(a_strip.lstrip())
print(b_strip.rstrip())
print(a_strip)
print(b_strip.strip())

a='Life is too SHORT'
print(a.replace("Life","SHORT"))
print(a)

print(a.split())
print(a.split('  '))
# lis = ['a','b','c','d']
# print(lis.split(':'))
print(a.split('o'))
