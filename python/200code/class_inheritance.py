class Add:
    def add(self,n1,n2):
        return n1+n2
class Multiply:
    def multiply(self,n1,n2):
        return n1*n2
class Calculate(Add,Multiply):
    def minus(self,n1,n2):
        return n1-n2
cal=Calculate()

print(cal.add(2,4))

print(cal.multiply(2,4))

print(cal.minus(2,4))


