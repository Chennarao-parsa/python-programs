n=int(input("enter a number:"))


while n>0:
    r=n%10
    fact=1
    while r>1:
        fact=fact*r
        r=r-1
    
        

  n=n//10
