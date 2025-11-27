'''n=int(input("Enter the no  of terms:"))
a=0
b=1
print(a,b,end=' ')

for i in range(1,n-1):
    c=a+b
    print(c,end=' ')
    a=b
    b=c
    '''
# Check whether given no is fib or not
'''
n=int(input("enter a number:"))
a=0
b=1
if n==0:
    print("fibonacii")
else:
    while b<n:
        c=a+b
        a=b
        b=c
    if c==n:
        print("fibonacii")
    else:
        print("Not  a fibonacii")
'''
'''
num=int(input("enter a number:"))
a=0
b=1

while True:
    if num==0:
        print("fibonacii:")
        break

    c=a+b
    if c==num:
        print("fibonacii")
        break
    if c>num:
        print("not a fibonacii")
        break
    a=b
    b=c
'''

# Strong number
'''
n=int(input("Enter a number:"))
bkp=n
s=0
while n>0:
    t=n%10
    f=1
    while t>1:
        f=f*t
        t-=1  
    
    s=s+f
    n=n//10
if s==bkp:
    print("strong")
else:
    print("not  a strong")
    '''
#Armstrong number
n=int(input("Enter a number:"))
temp=n
m=len(str(n))
s=0
while n>0:
    r=n%10
    s=s+r**m
    n=n//10
if s==temp:
    print("Armstrong")
else:
    print("NOt a Armstrong")



    
    
        
