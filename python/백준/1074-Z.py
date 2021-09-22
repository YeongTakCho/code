import sys
n,r,c=map(int,sys.stdin.readline().split())
state=0

#multiply- r=2, c=1
def Z(num,multiply):
    _state=0
    while num>0:
        doubles=1
        while num>=doubles*2:
            doubles*=2
        num-=doubles
        _state+=doubles**2*multiply
    return _state

state+=Z(r,2)
state+=Z(c,1)

print(state)
