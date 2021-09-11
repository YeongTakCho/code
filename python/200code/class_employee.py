class Employees:
    raise_amount=1.1
    def __init__(self,first,last,pay):
        print('Data is saved')
        self.first=first
        self.last=last
        self.pay=pay
    def full_name(self):
        return '{}{}'.format(self.first,self.last)
    def raise_pay(self):
        self.pay=self.pay*self.raise_amount
        print("{}'s raised pay is {} won".format(self.full_name(),self.pay))
em1 = Employees('cho','yeongtak',1000000000)
em2 = Employees('kim','seungun',1000000000)

em1.raise_amount=1.2

em1.raise_pay()
em2.raise_pay()


