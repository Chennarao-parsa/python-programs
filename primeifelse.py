'''n=int(input("enter a number:"))
c=0
i=1
while i<=n:
    if n%i==0:
        c+=1
    i+=1
if c==2:
    print("prime")
else:
    print("not a prime")
    '''
n=int(input("enter a number"))
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print("prime")
else:
    print("not a prime")
        
