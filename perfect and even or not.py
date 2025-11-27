n=int(input("Enter a number:"))

d=1
s=0

while d<=n//2:
    if n%d==0:
        s=s+d
    d=d+1
    

if s==n:
    if s%2==0:
        print("perfect and Even")
else:
    print("not perfect")
    
    
        
