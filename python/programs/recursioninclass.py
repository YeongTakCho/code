class test:
    def getNum(self):
        self.num = int(input())
    def recursion(self,num):
        if num > 0:
            print(num)
            num-=1
            self.recursion(num)

test_object = test()
test_object.getNum()
test_object.recursion(test_object.num)