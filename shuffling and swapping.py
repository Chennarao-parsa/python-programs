#swapppig
'''
a=10
b=20
a,b=b,a
print(a,b)
'''
#
'''
s1="hello"
s2="world"
s1,s2=s2,s1
print((s1,s2))
'''
#swap its first and last elements
'''
x=[1,2,3,4,5]
x[0],x[-1]=x[-1],x[0]
print(x)
'''
#swap the characters at positions i and j
'''
s="hello"
i=1
j=3
l=list(s)
l[1],l[3]=l[3],l[1]
print(''.join(l))
'''
#swap ele with even indices with the odd indices
'''
a=[1,2,3,4,5,6]
e=[i for i in a if i%2==0]
o=[j for j in a if j%2!=0]
y=[]
for c,d in zip(e,o):
    y.append(c)
    y.append(d)
print(y)
'''
# using for loop
'''
a=[1,2,3,4,5,6]
for i in range(0,len(a)-1,2):
    a[i],a[i+1]=a[i+1],a[i]
print(a)
'''
'''
#swap every pair of ele and reverse a list\
# Swap every pair of elements and reverse pair-wise order

lst = [1, 2, 3, 4, 5, 6]

# Step 1: Swap every pair
for i in range(0, len(lst) - 1, 2):
    lst[i], lst[i+1] = lst[i+1], lst[i]
print(lst)

# Step 2: Reverse the list in chunks of 2
result = []
for i in range(len(lst) - 2, -1, -2):
    result.extend(lst[i:i+2])

print("Final list:", result)
'''
#swap the midde ele
'''
x=[1,2,3,4,5]
y=['a','b','c','d','e']
x[2],y[2]=y[2],x[2]
print(x)
print(y)
'''
#reversing
'''
x=[1,2,3,4,5]
x.reverse()
print(x)
'''
#reversing2
'''
l1=[1,2,3,4,5]
n=len(l1)
for i in range(n-3):#N//2
     l1[i],l1[n-i-1]=l1[n-1-i],l[i]
print(l1)
'''
#<.................. SORTING  .............>
#sorting the ele in ascending
'''
x=[5,2,7,1,3]
print(sorted(x
'''
#2]
'''
x=[5,2,7,1,3]
x.sort()
print(x)
'''
#3
'''
x=[5,2,7,1,3]
for i in range(0,len(x)):
     for j in range(i+1,len(x)):
          if x[i]>x[j]:
               x[i],x[j]=x[j],x[i]
print(x)
'''
#list of strings alphabetically
#1
'''

l=['apple','banana','orange','grape','pear']
l.sort()
print(l)
'''
#2
'''
x=['apple','banana','orange','grape','pear']
for i in range(0,len(x)):
     for j in range(i+1,len(x)):
          if ord(x[i][0])>ord(x[j][0]):
               x[i],x[j]=x[j],x[i]
print(x)
'''
#sort them by their length
'''

x=['apple','banana','orange','grape','pear']
for i in range(0,len(x)):
     for j in range(i+1,len(x)):
          if len(x[i])>len(x[j]) or ord(x[i][0])>ord(x[j][0]):
               x[i],x[j]=x[j],x[i]

print(x)
'''
# sort the list of numbers in desecnding order
'''
x=[5,2,7,1,3]
x.sort()
print(x[::-1])
'''
#2
'''

x=[5,2,7,1,3]
for i in range(0,len(x)):
     for j in range(i+1,len(x)):
          if x[i]<x[j]:
               x[i],x[j]=x[j],x[i]
print(x)
'''
#3
'''
x=[5,2,7,1,3]
x=sorted(x,reverse=True)
print(x)
'''
#sort the tuples based onthe second element of every tuple
'''
l=[(1,5),(2,3),(3,8),(4,1),(5,6)]
for i in range(0,len(l)):
     for j in range(i+1,len(l)):
          if (l[i][1]>l[j][1]):
               l[i],l[j]=l[j],l[i]
print(l)

 '''
#sort them based on their last character
'''
x=['apple','banana','orange','grape','pear']
for i in range(0,len(x)):
     for j in range(i+1,len(x)):
          if ord(x[i][-1])>ord(x[j][-1]) or ord(x[i][0])>ord(x[j][0]):
               x[i],x[j]=x[j],x[i]
print(x)
'''
#sort the given list as integers to left and strings to right
'''
l=['apple','3','banana','1','orange','5']
l1=[]
l2=[]
for i in range(len(l)):
     if l[i].isalpha():
          l1.append(l[i])
     else:
          l2.append(i)
print(l1+l2)
'''
'''
l=['apple',3,'banana',1,'orange',5]
l1=[]
l2=[]
for i in l:
     if str(i).isdigit():
          l1.append(int(i))
     else:
          l2.append(i)
print(l2+sorted(l1))
'''
#even left odd right
'''
l=[5,2,8,1,7,4,3,6]
l1=[]
l2=[]
for i in l:
     if i%2==0:
          l1.append(i)
     else:
          l2.append(i)
print(sorted(l1)+sorted(l2))
'''
#vowels
x=['apple','banana','orange','grape','pear']
for i in x:
     for j in range(len(i)):
          print(j[0])
          

          
          


          
     






