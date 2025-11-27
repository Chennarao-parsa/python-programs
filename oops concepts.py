#oops
'''
class Firstclass:
    def display(self):
        print("hello people")
obj=Firstclass()
obj.display()
obj1=Firstclass()
obj1.display()
'''
#each object is diffeerent from others
#every object has its own memory
'''

class Prime:
    def __init__(self,n):
        self.num=n
    def isprime(self):
        for d in range(2,(self.num//2)+1):
            if self.num%d==0:
                return False
        else:
             return True
    def perfect(self):
        s=0
        for d in range(1,(self.num//2)+1):
            s=s+d
        if s==self.num:
            print("perfect",s)
        else:
            print("Not a perfect")
obj=Prime(7)
res=obj.isprime()
print(res)
res=obj.perfect()
print(res)
'''
#creating a class student
'''

class Student:
    institute='vcube'
    std_fees=[]
    def __init__(self,n,a,m1,m2,f):
        self.name=n
        self.age=a
        self.eng_marks=m1
        self.maths_marks=m2
        Student.std_fees.append(f)
    def info(self):
        print(self.name,self.age)
    def average(self):
        return (self.eng_marks+self.maths_marks)/2
    def getgrade(self):
        res=self.average()
        if res>80:
            grade='A'
        elif res>70:
            grade='B'
        elif res>55:
            grade-'c'
        else:
            grade='d'
        msg=f'{self.name} has secured grade is {grade}'
        return msg
        #decorating the class method
    @classmethod
    def getrevenue(cls):
        amt=0
        for i in cls.std_fees:
            amt=amt+i
        msg=f'{cls.institute} has generated {amt} revenue'
        return msg
        print('it is a class method')
        print(cls)
obj=Student('adhi',22,89,78,45000)
obj.info()
res=obj.getrevenue()
print(res)
print(obj.institute)#calling by using object
print(Student.institute)#calling by using the class name
print(Student.std_fees)
res=obj.getgrade()
print(res)
res=obj.average()
print(res)
'''
#Acess modifiers
'''
class Student:
    def __init__(self,n,a,m):
        self.name=n
        self._age=a
        self.__marks=m
    def info(self):
        print(self.name,self._age,self.__marks)
s1=Student('raju',36,90)
s1.name='siva'
s1._age=46
s1._Student__marks=78#name mangling
s1.info()
'''
#standard way of coding  is using setter and getter methods to change the private variables

'''class Student:
    def __init__(self,n,m):
        self.name=n
        self.__marks=m
    def info(self):
        print(self.name,self.__marks)
    def getmarks(self):
        return self.__marks#acess by outside
    def setmarks(self,m):#changing the value
        if m>0 and m<100:
            self.__marks=m

s1=Student('raju',56)
s1.setmarks(76)
print(s1.getmarks())
s1.info()
'''
# we treat methods as variables by @property



        
        





