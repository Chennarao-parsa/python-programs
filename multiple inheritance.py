#multiple inheritance
'''class Calc1:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        return self.a+self.b
class Calc2:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def multi(self):
        return self.x*self.y
class Calculator(Calc1,Calc2):
    def __init__(self,e,f):
        Calc1.__init__(self,e,f)
        Calc2.__init__(self,e,f)
obj=Calculator(10,20)
res=obj.addition()
print(res)
res=obj.multi()
print(res)
'''
