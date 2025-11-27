n=int(input("enter a no"))
sum=0

d=1
i=1
while i<=n:
    
    
    while d<=i//2:
            if i%d==0:
                sum=sum+d
            d=d+1
    if sum==i:
        print(i)
    i=i+1
   
    
    







































        
    
