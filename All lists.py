#max min elements
'''l=[1,23,3,4,4,45,5]
max=float("-inf")
min=float("+inf")
for i in l:
    if i>max:
        max=i
    if i<min:
        min=i
print("max value",max,"min value",min)"

'''
#Duplicats items.py
'''
l=[2,2,34,1,2,3,3,1]
l2=[]
for i in l:
    if i not in l2:
        l2.append(i)
print(l2)
'''
# Reveerse a list in python
'''
l=[1,2,3,4,5,67]
l2=[]
for i in range((len(l))-1,-1,-1):
    l2.append(l[i])
print(l2)
'''
#check list is empty
'''
l=[]
if not l:
    print("Empety")
else:
    print("not Empty")
    '''
#Index of  a specific element
'''
ele=int(input("enter a element:"))

x=[1,2,4,5,6,33]
for i in range(len(x)):
    if ele==x[i]:
        print(i)
    '''
#count occurence of a elem
'''
ele=int(input("enter a element:"))
count=0
x=[1,2,4,2,2,5,6,33]
for i in range(len(x)):
    if x[i]==ele:
        count=count+1
print(count)
'''
# merge two lists in python
'''
x=[1,2,4,2,2,5,6,33]
y=[1,2,4,2,2,5,6,33]
x.extend(y)
print(x)
'''
#sum of ele in a list
'''
x=[1,2,4,2,2,5,6,33]
s=0
for i in x:
    s=s+i
print(s)
'''
#remove element from a list by its value
'''
ele=int(input("enter a element:"))
x=[1,2,4,2,2,5,6,33]
for i in x:
    if i==ele:
        x.remove(i)
print(x)
'''
# if you remove all occurence of a elements use this method
'''
ele=int(input("enter a element:"))
x=[1,2,4,2,2,5,6,33]
l2=[]
for i in x:
    if i!=ele:
       l2.append(i)
print(l2)
'''
#slice to get specific elements
'''
x=[1,2,4,2,2,5,6,33]
y=x[2:]
print(y)
'''
#find a length of a list
'''
x=[1,2,4,2,2,5,6,33]
print(len(x))
'''
#ADD element at the end of  a list
'''
x=[1,2,4,2,2,5,6,33]
x.append(7)
print(x)'''
#Iterate through a list using for loop
'''
x=[1,2,4,2,2,5,6,33]
for i in x:
    print(i)
    '''
#Insert a element at a specific position
'''
x=[1,2,4,2,2,5,6,33]
print(len(x))
x.insert(1,88)
print(x)
print(len(x))
'''
#Extend a list with elements from another iterable
'''x = [1, 2, 3]
y = [4, 5, 6]

x = [*x, *y]  # creates a new extended list
print(x)
'''
'''
x = [1, 2, 3]
x.extend((3,4))
print(x)
'''
#Clear all elements from a list
"""
x=[1,2,4,2,2,5,6,33]
x.clear()
print(x)
"""

#creates a copy a list
'''
x=[1,2,4,2,2,5,6,33]
y=x
print(id(x))
print(id(y))
print(y)
print(x)
'''
'''
x = [1, 2, 3]
y = x.copy()
print(y)  
print(x is y)
'''
#index of a specific element
'''
x = [10, 20, 30, 20]
print(x.index(20))
'''
#insert at a specific position
'''
x = [1, 2, 3]
x.insert(1, 99)  
print(x)
'''
#reverse a list
'''
x = [1, 2, 3]
x.reverse()
print(x) 
'''
# sort a list
'''
x = [1, 2, 3,7,2]
y=[]
x.sort()
print(x)
'''
#reverse a listin place (modify original)
"""
x = [1, 2, 3]
x[:]=x[::-1]
print(x)
"""
# find the index of first occurence of a element from a specific position
"""
ele=int(input("enter a elemen"))
pos=int(input("enter a position"))
x=[1,3,4,3,4,1,2,7,8]
for i in range(pos,len(x)):
    if x[i]==ele:
        print(i)
        break
else:
    print("ele not found")
    """

#REmove and returm last ele from a list
'''
x=[2,4,5,6,7,8]
x1=[]
for i in range(len(x)):
    if i==len(x)-1:
        x1=x[i]
print(x1)
x=x[:len(x)-1:1]
print(x)
'''
'''
x=[1,4,6,78,6,9]
x[:]=x[::-1]
print(x)
x.remove(x[0])
print(x)
'''
#find the index of the last occurence of a element from a list
'''
ele=int(input("enter a element"))
last=-1
x=[2,4,5,6,7,8,2]
for i in range(len(x)):
    if ele==x[i]:
        last=i
if last!=-1:
    print("Last occurence of index",last)
else:
    print("not found")

'''
# check two lists are equal
'''
x=[1,4,6,78,6,9]
y=[1,4,6,78,6,9]
if len(x)== len(y):
    for i in range(len(x)):
        if x[i]!=y[i]:
            print("not equal")
            break
    else:
        print("Equal")
else:
    print("Not Equal")
    '''
  
'''
x = [1, 2, 3]
y = [1, 2, 6]

if x==y:
    print("EquaL")
else:
    print("Not Equal")
    
'''
#Program to find the duplicates from a list
'''
l=[1,4,3,4,3,3,1,7,8]
l2=[]
for i in range(len(l)):
    if l.count(l[i])>1 and l[i] not in l2:
        l2.append(l[i])
        
print(l2)
'''
'''
#2
l=[1,4,3,4,3,3,1,7,8]
l.sort()
l1=[]
for i in range(len(l)-1):
    if l[i]==l[i+1] and  l[i] not in l1:
        l1.append(l[i])
        
print(l1)
'''
#find dulpicates in LIST
'''
l=[1,3,5,6,7,3,5]
l1=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[j] and l[i] not in l1:
            l1.append(l[i])
print(l1)
      '''
#second occurence of a given element in a list
'''
ele=int(input("Enter  a element:"))
l=[1,3,4,5,1,4,56,5,6,1]
count=0
sec=-1
for i in range(len(l)):
    if l[i]==ele:
        count=count+1
        if count==2:
            sec=i
if sec!=-1:
    print("second occurence",sec)
else:
    print("ele not found")
    '''
#Common functions
    #sorted 
'''   
x=[1,43,41,6,5]
output=sorted(x)
print(output)
print(x)
print(id(x))
print(id(output))
'''

#all and any
'''
x=[10,5,3,-1]
res=all(x)
print(res)


# any
x=[-1,1,0,0]
res=any(x)
print(res)
'''

#give list is a palindrome or not
'''
l=[1,2,3,2,1]
if l==l[::-1]:
    print("True")
else:
    print("False")
    '''

#list comprehension to get all even numbers from  1to 20
'''
l=[i for i in range(1,21) if i%2==0]
print(l)

'''
#program to split a list into chunks of a given size
'''
l=[1,2,3,4,5,6]
c_size=2
chunks = []

for i in range(0, len(l), c_size):
    chunk = l[i:i + c_size]
    chunks.append(chunk)

print(chunks)
# sort a list in ascending using bubbble sort algorithm
'''
'''
l=[5,2,9,1,5,6]







'''
#difference between max and mun element in a list
'''
l=[10,20,5,8]
max=float("-inf")
min=float("+inf")
for i in l:
    if i>max:
        max=i
    if i<min:
        min=i
print("diffrence between max and min elements:",max-min)
'''
# program to fingd the first repeating ele in a list
'''
l=[10,5,3,4,3,5,6]
for i in range(len(l)):
    if l.count(l[i])>1:
        val=l[i]
        break
print(val)
'''
#program to find the all perfect no in a list
"""
l=[6,28,12,496,100]
l2=[]

for i in l:
    s=0
    for d in range(1,(i//2)+1):
        if i%d==0:
            s=s+d
        

    if s==i:
        l2.append(i)
print(l2)




"""
'''
#sorting list in a ascending order using Bubble sort
l=[5,2,9,1,5,6]
for i in range(0,len(l)):
    for j in range(0,len(l)-1-i):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)

'''
# Replacement using Slicing
'''
x=[10,23,33,5,6,7,7888]
x[1:3]=[200,34,88888,6666,56,78]
print(x)
'''
#Even no's from  a list
'''
output=[i for i in range(1,11)if i%2==0]
print(output)
'''

#squaring for even no's and cubing of odd numbers
'''
output=[i**2 if i%2==0 else i**3 for i in range(1,11)]
print(output)s=0]
'''
#withpout slicing sumn of the given numbers
'''
x=[3,33,333,3,333,355,5,5,55]
s=0
for i in x:
    s=s+i
print(s)
'''
#sort a list in a ascending order
'''
l=[34,5,677,7,7]
l.sort()
print(l)
'''
#print the ele which appers only once
'''
l=[1,2,2,3,4,4,5]
l2=[]
for i in l:
    if l.count(i)==1:
        l2.append(i)

print(l2)
        
'''
# replace negative no to 0 using list comprehension
l=[-1,2,-3,4,-5]
l1=[0 if i<0 else i for i in l ]
print(l1)
    
    



























                                               







    

        
