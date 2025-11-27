n=int(input("enter a number"))
i=1
sum=0
while i<=n:
    count=0
    d=2
    while d<=i//2:
        if i%d==0:
            count=count+1  
        d=d+1
    if count==0:
        print(i)
        sum+=i
    i+=1
print(sum)
