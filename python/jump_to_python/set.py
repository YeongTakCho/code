s1= set([1,2,3])
print(s1)
s2=set('hello')
print(s2)

#feature: unordered, no overlap

# print(s1[0]) :error code : set is unordered -> no index

l1=list(s1)
print(l1)
print(l1[0])

p1=tuple(s1)
print(p1)
print(p1[0])

l2=list(s2)
print(l2)
print(l2[0])

#1. 교집합
s1= set([1,2,3,4,5,6])
s2= set([4,5,6,7,8,9])
print(s1&s2)
print(s1.intersection(s2))

#2. 합집합
print(s1|s2)
print(s1.union(s2))

#3. 차집합
print(s1 - s2)
print(s2 - s1)
print(s1.difference(s2))
print(s2.difference(s1))

#set functions

#.add 값 추가
s1= set([1,2,3])
s1.add(4)
print(s1)

#.update 값 여러개 추가
s1.update([5,6,7])
print(s1)
# s1.update(8): errorcode : num(x)
s1.update([8,'9']) #list (o)
print(s1)
s1.update('123') #str (o)
print(s1)
s1.update((11,12,13)) #tuple (o)
print(s1)

#.remove 특정 값 제거하기
s1=set([1,2,3])
s1.remove(1)
# s1.remove(4) : errorcode : if no element -> error
print(s1)
