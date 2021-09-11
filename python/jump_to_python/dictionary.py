dic = {'name':'tak','phone':'01097181234','birth':'1120'}
print(dic)
print(dic['birth'])
dic['name']= 'yeong'
print(dic['name'])

num_dic={1:'one', 2:'two'}
print(num_dic[1])

lis_dic={1:[1,2,3]}
print(lis_dic[1][2])

dic = {1:'a'}
dic[2]= 'b'
dic['hello']='bye'
print(dic)
del dic['hello']
print(dic)
#dictionary는 오직 key로만 호출받는다
#key : char,str,num ( o) list (x) tuple (o) dictionary (x)
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(list(a.keys())) #.keys : return dic_keys[] 
#(can use as list without using list(): dic_keys, dict_valuse,dict_items)
print(a.values())
print(a.items()) #return dict_items([(key1:value1),(keys2:value2)])

print(a.get('name')) 
#using .get reason = if a['name'] isn't exist -> a['name'] makes error but get() return None 
print(a.get('age'))
print(a.get('age','no age data')) #get(find_key, return data if key_value isn't exist)

print('name' in a)
