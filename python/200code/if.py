x= [1,2,3]
if 1 in x:
    print('x')
for x_data in x:
    if x_data ==1:
        print('1')
for x_data in x*3:
    if x_data==1:
        print('1')
listdata = [1,2,[3,4,5]]
for list_data in listdata:
    if type(list_data)==list:
        for list_data_data in list_data:
            print(list_data_data)
    else:
        print(list_data)
str1='time is money'
for str1_data in str1*3 + str1[3:5]:
    print(str1_data)
    