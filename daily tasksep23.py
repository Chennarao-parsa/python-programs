#bank
'''
class Bankaccount:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
b=Bankaccount(1000)
b.deposit(500)
print(b.balance)
'''
#create a clas
'''
class Calculator:
    def __init__(self,a,b):
        self.x=a
        self.y=b

    def add(self):
        return self.x+self.y
    def sub(self):
        return self.x-self.y
    def multiply(self):
        return self.x*self.y
    def divide(self):
        return self.x/self.y
obj=Calculator(10,20)
res=obj.add()
print(res)
res=obj.sub()
print(res)
res=obj.multiply()
print(res)
res=obj.divide()
print(res)
'''
#pattern
'''
n=int(input("enter number of rows:"))
num=1
for i in range(1,n+1):
    for j in range(i):
        print(num,end=' ')
        num=num+1
    print()
    '''
n=int(input("enter a number:"))
num=5
for i in range(1,n+1):
    for j in range(n,n-i,-1):
        print(j,end=' ')
    print()
        
    
    
    
        
        

              
        
        
