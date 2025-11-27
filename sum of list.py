"""l=[1,3,4,445,56]
s=0

for i in l:
    s=s+i
print(s)
"""
'''
x=[10,20,56,67,589,67]
max_value=float('-inf')

for i in x:
    if i>max_value:
        max_value=i
print(max_value)
'''
'''

x=[10,20,56,67,589,67]
small_val=float('+inf')
for i in x:
    if i<small_val:
        small_val=i
print(small_val)
'''
'''
x=[11,13,15,24,24,3444]
n=int(input("enter a number"))
if n in x:
    print("yes")
else:
    print("no")
    '''
n=int(input("enter a number:"))
s=0
for  i in range(1,(n//2)+1):
    if n%i==0:
        s=s+i
if n==s:
    print("perfect")
else:
    print("not perfect")
    
    
        
