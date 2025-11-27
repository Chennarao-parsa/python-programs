n=int(input("enter a number;"))
temp=n
s=0
c=0
while n>0:
    n=n//10
    c=c+1
n=temp   
while n>0:
    r=n%10
    s=s+r**c
    n=n//10
if s==temp:
    print("armstong")
else:
    print("Not Armstrong")
