def print_fifth_num(*nums):
    try:
        print(nums[4])
    except Exception as e:
        print('no fifth num')
        print(e)
    else:
        print('no error')
print_fifth_num(1,2,3,4)

from time import sleep
count =1
try:
    while(True):
        print(count)
        count +=1
except KeyboardInterrupt:
    print('ctrl c is clicked... program stopped')