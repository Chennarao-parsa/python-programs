n=int(input("Enter a even fibonacii number you want:"))
a=0
b=1
cnt=0
while True:
    c=a+b
    if c%2==0:
        cnt=cnt+1
        if cnt==n:
            print(c)
            break
    a=b
    b=c
    

            
