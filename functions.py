'''
#1 dispaly fun
def fun():
     print("how are you")
fun()
'''
#2 parameters
'''
def add(a,b):
     return a+b
res=add(10,80)
print(res)
'''
#3 default
'''
def add(a=10,b=90):
     return a+b
res=add(20,89)
print(res)
'''
#4 docstring
'''

def docstring(s):
     # hello this is a docstring
     return s
print(docstring(10))
'''
#scope
#local
'''

def local():
     a=20
     print(a)
local()
'''
#nonlocal
'''
y=20
def add():
     a=20
     def add1():
          b=10
          return(a+y+b)
     
     return add1()
m=add()
print(m)
'''
#global scope
'''
y=10
def add():
     x=30
     def add1():
          z=20
          print(x)
          print(z)
     add1()
     
print(y)
add()
print(y)
'''
#lambda functions
#square of a number
'''
x=[1,2,3,4,5,6]
s=list(map(lambda a:a**2,x))
print(s)
'''
#Adding the two numbers
'''

add=lambda a,b:a+b
res=add(10,20)
print(res)
     '''
#for individual square
'''
res=lambda n:n**2
print(res(2))
'''
#maximum of two numbers in python
'''
res=lambda a,b : a if a>b else b
print(res(10,20))
'''
























