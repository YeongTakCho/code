str='[1,2,3,4]';str=str.replace('[','');str=str.replace(']','')
str=str.split(',')
print(str)
print(type(str))
print(str[0])
print(type(str[0]))