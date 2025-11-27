'''
#Creating a tuple
t=(10,30,'vcube',True,'python',10)
print(t)

#slicing a tuple
res=t[0:2]
print(res)
'''
'''
# Logical Questions
t=(90)
print(type(t))
# log2
t=(90,)
print(type(t))

#Logical 3
t=1,2,3,5
print(t)
'''

#Modifying a tuple is not possible but you can rewrite it
'''
t=(1,4,5,6,7,7)
print(id(t))
li=list(t)
li.append(90)
t=tuple(li)
print(t)
print(id(t))
'''
# Unpacking
'''
l=[10,30]
a,b=l
print("a=",a,"b=",b)


l=[10,30,40,59,89,90]
a,b,*c=l
print("a=",a,"b=",b,"c=",c)
'''

# Spreading as a individ\ual
'''
l=[10,30,40,59,89,90]
print(*l)
#Add 100 to the list witout apppend
l=[10,30,40,59,89,90]
y=[*l,100]
print(y)
'''
# Unique pairs from a given list whose sum is equal to the 6
'''
x=[1,2,3,4,5]
target=6
l2=[]
for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i]+x[j]==target:
            print([x[i],x[j]],end='')
 '''           '''
#Create a tuple with the  single element
t=(1,)
print(t)
print(type(t))
#how do you access a tuple
t=(3,1,4,56,6)
print(t[3])
'''
'''
#Access first element from a given tuple
t=(1,2,34,4,4)
print(t[0])
#concatenate the two tuples
t=(2,34,4,4)
t1=(4,5,4,4,69,0)
print(t+t1)
'''
#max and min ele in atuple
'''
t=(6,4,5,8,99)
max=float("-inf")
min=float("+inf")

for i in t:
    if i>max:
        max=i
    if i<min:
        min=i
print("max:",max,",","min:",min)'''
#tuple methods
'''
#count
t=(34,4,4,56,4,35)

print(t.count(4))
# index method
t=(34,4,4,56,4,35)
print(t.index(4,2,5))
'''
# program to remove specific ele in a tuple
'''
t=(1,2,3,2)
ele =int(input("enter a element:"))
'''
'''
t1=()
for i in t:
    if i!=ele:
        t1=t1+(i,)
print(t1)
'''
'''
l=[]
for i in t:
    if i!=ele:
        l.append(i)
n=tuple(l)
print(n)
'''
#write a program to multiply all elements of a tuple
'''
t=(2,3,4)
s=1
for i in t:
    s=s*i
print(s)
'''
#python program to remove dulpicates from a tuple
'''
t=(1,2,2,3)
l2=[]
for i in t:
    if i not in l2:
        l2.append(i)
l3=tuple(l2)
print(l3)
'''
# python program to sort the elements in a Ascending order
'''
m=tuple(map(int,input("enter  a number separed by space:").split()))
print(m)
t=list(m)
for i in range(len(t)):
    for j in range(len(t)-1-i):
        if t[j]>t[j+1]:
            t[j],t[j+1]=t[j+1],t[j]
m1=tuple(t)
print(m1)
'''
#another
'''
m=tuple(map(int,input("enter a number you want sort it:").split()))
n=list(m)
n.sort(reverse=True)
m1=tuple(n)
print(m1)
'''
# list comprehension of all even no's from 1 to 20
'''
l=[i for i in range(1,21) if i%2==0]
print(l)
'''
#squares of a even no s from list using list comprehension
'''
n=int(input("enter a no"))
l=[i**2 for i in range(1,n) if i%2==0]
print(l)
'''
#flatten tuples into a single tuple
t=((1,2),(3,4),(5,))
f=()
for i in t:
    f=f+i
print(f)
# tuple into flatten tuples
t=(1,2,3,4,5,6)
size=2
tuples=[tuple(t[i:i+size])for i in range(0,len(t),size)]
print(tuples)
        


  
    
    
    
    
