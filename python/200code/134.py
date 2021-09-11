exprl1='2+3'
# exprl2='''for i in range(10)
#     print("%d",%i)
# '''

eval(exprl1)
# eval(exprl2)
# print(help(eval))

funcs=[lambda x: x+1, lambda x: x*2]
print(funcs[0](3), funcs[1](7))

f=lambda x,y: (x**x)+y
args=[[4,5,2,3,5],[2,2,6,1,7]]
ret=map(f,args[0],args[1])
print(type(f)) #class 'function'
print(type(ret)) #class 'map'
print(ret) #trash data
print(list(ret));print()

f= lambda x,y: x*x+y
args=[[1,2,3,4,5],[5,4,3,2,1]]
ret=map(f,args[0],args[1])
print(list(ret))