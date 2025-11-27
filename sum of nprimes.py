#n primes numbers sum
n=int(input("enter  a n :"))
count=0
sum=0

num=2
while True:
    
    d=2
    
    while d<=num//2:
        if num%d==0:
            break
        d=d+1
    else:
        print(num)
        sum=sum+num
        count=count+1
        
        if count==n:
            break
    num=num+1
print(sum)

     
        
