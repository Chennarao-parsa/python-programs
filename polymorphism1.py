#1
'''
class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def calculate_area(self):
        return self.length*self.breadth
class Circle:
    def __init__(self,r):
        self.radius=r
        self.pi=3.14
    def calculate_area(self):
        return self.pi*(self.radius*self.radius)
sets=[Rectangle(4,5),Circle(4)]
for i in sets:
    print(i.calculate_area())
    '''
#2
'''
class Car:
    def num_of_vehicles(self):
        print("car has 4 wheels")
class Bike:
    def num_of_vehicles(self):
        print("Bike has a 2 wheels")
obj1=Car()
obj2=Bike()
l=[obj1,obj2]
for i in l:
    i.num_of_vehicles()
    '''
#3
class Vehicle:
    def capacity(self):
        print("vehicle")
        
class Bus:
    def capacity(self):
        print("Bus can carry multiple passengers")
class Car:
    def capacity(self):
        print("car is meant for only few passengers")
obj1=Vehicle()
obj2=Bus()
obj3=Car()
l=[obj1,obj2,obj3]
for i in l:
    i.capacity()
    
    
    
        
        
