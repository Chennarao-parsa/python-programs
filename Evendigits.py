#evenn digits
n=int(input("Enter a number"))
s=0
while n>0:
    r=n%10
    if n%2==0:
        s=s+r
    n=n//10
print(s)

    
