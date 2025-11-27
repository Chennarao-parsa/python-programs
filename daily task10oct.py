#sum of first n Natuaral no using recursion
'''
def natural(n):
    if n==1:
        return 1
    return n+natural(n-1)
res=natural(10)
print(res)
'''
#sum of digits of a number
'''
def sumofdigit(n):
    if n==0:
        return 0
    return n%10+sumofdigit(n//10)
res=sumofdigit(1234)
print(res)
'''
#inheritance
class Animal:
    def sound(self):
        print("sound of animal")
class Dog(Animal):
    
    
    
