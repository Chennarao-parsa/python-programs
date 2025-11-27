n=int(input("Enter a Number"))
count=0      
while n>0:
    r=n%10
    if r==0:
        count=count+1
    n=n//10
print(count)
