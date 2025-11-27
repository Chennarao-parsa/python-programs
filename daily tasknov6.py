#sum of ele
'''
l=[1,2,3,4,5]
s=0
for i in l:
    s=s+i
print(s)
'''
#count even and odd numbers in A LIst
'''
l=[1,2,3,4,5]
even_count=0
odd_count=0
for i in l:
    if i%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print("even",even_count)
print("odd",odd_count)
'''
#largest ele in a list
'''
l=[10,20,5,90,56]
large=float('-inf')

for i in l:
    if i>large:
        large=i
print(large)
        '''
#number ofoccurecde of  a specific ele
'''
l=[1,2,3,2,2,4]
ele=int(input("enter a ele:"))
cnt=0
for i in l:
    if i==ele:
        cnt+=1
print(cnt)
'''
#remove the duplicates from a list
'''
l=[1,2,2,3,4,4]
l2=[]
for i in l:
    if i not in l2:
        l2.append(i)

print(l2)
'''
#reverse a list without using any string functions
'''
l=[10,20,30,40,50]
l2=[]
for i in range(len(l)-1,-1,-1):
    l2.append(l[i])
print(l2)
'''
#palindrome
'''
l=[1,2,3,2,1]
if l==l[::-1]:
    print(True)
else:
    print(False)
    
'''
#concatenate two lists without using extend method
'''
a=[1,2,3]
b=[4,5,6]

for i in b:
    
    a.append(i)
print(a)
'''
#or
'''
a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)
'''
#second largest in  a list without using  built in functions
'''
l=[10,20,4,45,99,99]
lar=float('-inf')
slarge=float('-inf')
for i in l:
    if i>lar:
        slar=lar
        lar=i
    elif i>slar and i<lar:
        slar=i
print(slar)
'''
#to insert an ele at a specific index
'''
l=[1,2,4]
l.insert(2,3)
print(l)
'''
#replace last ele of each sublist in a 2D with 0
l=[[1,2],[3,4],[5,6]]
val=0
for i in l:
    i[-1]=val
print(l)
    
    

                 
