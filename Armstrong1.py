n=int(input("Entr a number:"))
s=0
bkp=n
while n>0:
    t=n%10
    f=1
    while t>0:
        f=f*t
        t=t-1
    s=s+f
    n=n//10
    
if bkp==s:
    print("Strong")
else:
    print("Not strong")
