#membership operators
'''
x=[10,20,'vcube',True,'python']
res=20 in x
re=30 in x
print(res)

print(re)
'''
#short hand evolution operator
'''
n=int(input("enter a number:"))
print("Even")if n%2==0 else print("odd")
'''
#loops
'''
i=1
while i<=5:
    print(i)
    i=i+1
    '''
# sum of natural numbers for a given number
'''
n=int(input("enter a number:"))#6
s=0
i=1
while i<=n:
    s=s+i
    i=i+1
print("sum of natural numbers",s)
'''
#divisors of a given number
'''
n=int(input("enter a number:"))
d=1
while d<=n:
    if n%d==0:
        print(d)
    d=d+1
    '''
#prime or not
n=int(input("enter a number:"))
d=1
c=0
import time
start=time.time()
while d<=n:
    if n%d==0:
        c=c+1
    d=d+1
if c==2:
    print("prime")
    
else:
    print("not a prime")
end=time.time()
print("Time taken by this ",end-start)
# prime simple

    


