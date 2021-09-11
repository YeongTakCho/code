from time import sleep
help(print)
for i in range(10):
    print('%d'%i,end= ' ',flush=True)
    sleep(1)