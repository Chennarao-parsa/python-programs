class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def info(self):
        print(f"Name:{self.name},Age:{self.age}")
class Student(Person):
    def __init__(self,name,age,roll_no,marks):
        super().__init__(name,age)
        self.roll_no=roll_no
        self.marks=marks
    def info(self):
        super().info()
        print(f"Roll_no:{self.roll_no},Marks:{self.marks}")
s1=Student("tarun",20,90,95)
s1.info()
        
