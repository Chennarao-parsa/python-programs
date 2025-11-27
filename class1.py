#program1
'''
class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def display(self):
        print(self.name,self.age)
obj=Person('Harsha',45)
obj.display()
obj1=Person("ram",67)
obj1.display()
'''
#calculator
'''
class Calculator:
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def addition(self):
        return self.x+self.y
    def mul(self):
        return self.x*self.y
    def sub(self):
        return self.x-self.y
    def div(self):
        return self.x/self.y
obj=Calculator(15,5)
res=obj.addition()
print(res)
res=obj.mul()
print(res)
res=obj.sub()
print(res)
res=obj.div()
print(res)
'''
#recursive function of factorial
'''
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
res=factorial(5)
print(res)
'''
#recursive sum of the natural numbers
'''
def sumofnatural(n):
    if n==1:
        return 1
    return n+sumofnatural(n-1)
res=sumofnatural(5)
print(res)
'''
#rectangle
class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
obj=Rectangle(5,7)
print(obj.area())
print(obj.perimeter())

