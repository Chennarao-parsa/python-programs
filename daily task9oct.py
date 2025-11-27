#inheritance
'''
class Animal:
    def sound(self):
        print("Animals makes different sounds")
class Dog(Animal):
    def sound(self):
        print("dog sound like bowww")
class Cat(Animal):
    def sound(self):
        print("cat sounds like mewww")
obj=Animal()
obj.sound()
d=Dog()
d.sound()
c=Cat()
c.sound()
'''
#2
'''
class Vehicle:
    def type_of_vehicle(self):
        print("type of the vehicle")
class Bike(Vehicle):
    def type_of_vehicle(self):
        print("Bike is 2 wheeler")
class Car(Vehicle):
    def type_of_vehicle(self):
        print("car is 4 wheeler")
obj=Vehicle()
obj.type_of_vehicle()
b=Bike()
b.type_of_vehicle()
c=Car()
c.type_of_vehicle()
'''
#3
'''
class Fruit:
    def taste(self):
        print("taste of different fruits")
class Apple(Fruit):
    def taste(self):
        print("Apple taste is sweet")
class Orange(Fruit):
    def taste(self):
        print("orange taste is sour")
f=Fruit()
f.taste()
a=Apple()
a.taste()
o=Orange()
o.taste()
'''
#sum of first n natural numbers
'''
def naturalnosum(n):
    if n==1:
        return 1
    return n+naturalnosum(n-1)
res=naturalnosum(10)
print(res)
'''
#sum of digits of a number using the recursion
def sumofdigit(n):
    if n==0:
        return 0
    return (n%10+sumofdigit(n//10))
res=sumofdigit(440)
print(res)
    
