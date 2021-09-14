import math
def canGoChannel(n):
    global enablebutton
    for i in str(n):
        if int(i) not in enablebutton:
            return 1
    return 0



enablebutton=[0,1,2,3,4,5,6,7,8,9]
print(canGoChannel(1234))