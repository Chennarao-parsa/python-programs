#rectangle
'''
class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
obj=Rectangle(5,6)
print(obj.area())
print(obj.perimeter())
'''
#person
'''
class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def info(self):
        print(self.name,self.age)
obj=Person("raj",24)
obj.info()
'''
#arithmetic opetations
'''
class Arithmetic:
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def add(self):
        print(self.x+self.y)
    def multi(self):
        print(self.x*self.y)
    def sub(self):
        print(self.x-self.y)
    def div(self):
        print(self.x/self.y)
    def mod(self):
        print(self.x%self.y)
obj=Arithmetic(10,5)
obj.add()
obj.multi()
obj.sub()
obj.div()
obj.mod()
'''
#student class
'''
class Student:
    def __init__(self,name,no,m1,m2,m3):
        self.name=name
        self.roll_no=no
        self.marks1=m1
        self.marks2=m2
        self.marks3=m3

    def average(self):
        avg=(self.marks1+self.marks2+self.marks3)/3
        return avg
    def display(self):
        print(f"Name :{self.name}")
        print(f"roll no :{self.roll_no}")
        print(f"marks :{self.marks1,self.marks2,self.marks3}")
        print(f"average :{self.average()}")
              
obj=Student('akil',4,90,47,88)
obj.display()

'''
#Bank account
'''
class Bankacc:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amt):
        if amt>0:
            
            self.balance=self.balance+amt
            print("after deposit",self.balance)
        else:
            print("Invalid deposit")
    def withdraw(self,amt):
        if amt>self.balance:
            print("Insuffient funds")
        elif amt<=0:
            print("Invalid with draw not possible")
        else:
            
            self.balance=self.balance-amt
            print(" after withdrawal ",self.balance)
    def checkbal(self):
        print("curretn available balance",self.balance)
b=Bankacc(10000)
b.deposit(5000)
b.withdraw(8000)
b.checkbal()
'''
