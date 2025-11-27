import random
i=1
while i<=10:
    
    n=random.randint(1,200)
    
    temp=n
    count=0
    s=0
   

    while n>0:
        
        n=n//10
        count=count+1
    n=temp
    while n>0:
        t=n%10
        s=s+t**count
        n=n//10
    if temp==s:
        print("Armstrong",temp)
    else:
        print("not Armstrong",temp)
    i=i+1
    
