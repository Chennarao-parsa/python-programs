n=int(input("Enter a number:"))
a=0
b=1
i=1
print(a,b,end=' ')
while i<=n-2:
    c=a+b
    print(c,end=' ')
    a=b
    b=c
    i+=1
    
