a= list()
print(a)
b=[1,2,'3',[1,2,'3',[1,2,'three']]]
print(b)
print(b[3])
print(b[3][3])
print(b[3][3][2])

a="12345"
print(a)
print(a[0:2])

a=['1','2','3','4','5']
print(a)
print(a[0:2])

a=[1,2,3,4,5]
print(a)
print(a[0:2])

b=a[0:2]
print(b)
#################################################
# list or str funs
#return: no - del append sort reverse insert remove extend
#return: yes - index pop(but element is also changed) count
a=[1,2,3]
b=[4,5,6]
del b[1]
b.append(8)
a.insert(0,18)
print(a+b)
a[2]=7
a.remove(18) #if not -> error
a.pop() #가장 마지막 위치의 요소를 제거
a.pop(0) #0번 자리의 요소를 제거
print(a+b)
print('4 in a+b is on %d'%(a+b).index(4))
 # print((a+b).sort()) print= None -> .sort return None
print('len: %d'%len(a+b))

a='abc'
b='def'
# del b[1] error code
print(a+b)
# b.append('h') error code
# a[2]='g' error code
# str replace : NO!
# a.reverse() error code
# print('b in abc is on %d'%(a.index(b))) error code
print(a)
print(a.count('a')) #wow! it works
print('len: %d'%len(a+b))

a=['a','b','c']
b=['d','e','f']
del b[1]
b.append('k')
print(a+b)
a[2]='g'
print(a+b)
print('len: %d'%len(a+b))
print(a*3)

a=['abc','ade','abcd']
a.sort()
print(a) #wow!! it works!
a.reverse()
print(a)

a=['aaaa','a','abcdefg']
print(a.count('a')) #return 1
a.extend([4,5]) #extend 는 리스트만이 요소로 올 수 있다
print(a)