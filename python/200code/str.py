from time import sleep
for i in range(100):
    msg='\rpersent%d%%'%(i+1)
    print(' '*len(msg),end='')
    print(msg,end='')
    sleep(0.1)
def my_func():
    print('hello world')
list4=[1,2,3,my_func]
list4[3]()