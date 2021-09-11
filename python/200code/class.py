class MyClass:
    def __init__(self,txt):
        self.var='hello'
        print('MyClass instanse is created Name:%s'%txt)
    def __del__(self):
        print('MyClass instanse is deleted')
obj= MyClass('jessica')
print(obj.var)
obj.var='nice to meet you'
print(obj.var)
del obj