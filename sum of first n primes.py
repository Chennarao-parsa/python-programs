n=int(input("enter a number:"))
count=0
sum=0
num=2
while count<n:
    i=2
    p=1
    while i<=num//2:
        if num%i==0:
            break
        i=i+1
    if p==1:
        sum=sum+num
        count=count+1
    num=num+1
print(sum)
        
        
