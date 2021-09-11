import random

listdata =list(range(10))
for i in range(3):
    random.shuffle(listdata)
    print(listdata)

solarsys1=['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
ret=list(enumerate(solarsys1,start=1))
print(ret)
print(type(enumerate(solarsys1))) #class 'enumerate'

for i, body in ret:
    print('%d. %s --'%(i,body))

list_n=list(range(20,50,4))
print(sum(list_n))

solarsys2=['sun','mercury','venus','earth','mars','jupiter','saturn','uranus','pluto']

solarsys_en=enumerate(solarsys1)
solar_dict={}
for i, body in solarsys_en:
    solar_dict[solarsys2[i]]=body
print(solar_dict)

solar_dict['Sun']=solar_dict['sun']
del solar_dict['sun']
print(solar_dict)

keys=solar_dict.keys()
values=solar_dict.values()
items=solar_dict.items()

print(type(keys)) #class 'dict_keys'
print(type(values)) #class 'dict_values
print(type(items)) #class 'dict_items'
print(keys);print()
print(values);print()
print(items);print()
print(list(keys));print()
print(list(values));print()
print(list(items));print()

find_planet='mercury'

if find_planet in solar_dict:
    print("%s is in sloar system: %s"%(find_planet,solar_dict[find_planet]))
else:
    print("there are no planet you find")

ret1= sorted(solar_dict,len,reverse=True)
print(solar_dict)
print(ret1)

