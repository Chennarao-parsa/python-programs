class Student:
    institute='Vcube'
    std_fees=[]
    def __init__(self,n,a,m1,m2,f):
        self.name=n
        self.age=a
        self.english_marks=m1
        self.maths_marks=m2
        Student.std_fees.append(f)
    def info(self):
        print(self.name,self.age)
    def getaverage(self):
        return (self.english_marks+self.maths_marks)/2
    def getgrade(self):
        avg=self.getaverage()
        if avg>70:
            grade='A'
        elif avg>60:
            grade='B'
        else:
            grade='C'
        msg=f'{self.name} has secured {grade} grade'
        return msg
s1=Student('raju',36,67,89,45000)
s2=Student('ramu',37,89,98,56000)
s1.info()
s2.info()
res=s1.getaverage()
print(res)
res=s1.getgrade()
print(res)
print(s1.institute)
print(s2.institute)
print(Student.institute)
print(Student.std_fees)
