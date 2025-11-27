class Human:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def info(self):
        print(self.name,self.age)
class Employee(Human):
    def __init__(self,n,a,eno,salary):
        super().__init__(n,a)
        self.empno=eno
        self.salary=salary
    def info(self):
        super().info()
        print(self.empno,self.salary)
class Manager(Employee):
    def __init__(self,n,a,eno,salary,rights):
        super().__init__(n,a,eno,salary)
        self.rights=rights
    def info(self):
        super().info()
        print(self.rights)
obj=Manager('raju',36,1,100000,'special')
obj.info()
