# Given number is not fibonacii or not
n=int(input("enter a number:"))
a=0
b=1
while True:# if we dont know the no of iterations 
    c=a+b
    if c==n:
        print("fibonacii")
        break

    if c>n:
        print("Not Fibonacii")
        break
    a=b
    b=c
    
    
    
    

                
