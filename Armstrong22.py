n=int(input("Enter:"))
s=0
bkp=n
count=0
while n>0:
    n=n//10
    count=count+1
n=bkp
while n>0:
    r=n%10
    s=s+r**count
    n=n//10
if s==bkp:
    print("Armstrong")
else:
    print("not arm")
