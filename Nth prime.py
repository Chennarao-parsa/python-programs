n=int(input("Enter a number:"))
count=0
num=2
while True:
    d=2
    while d<=num//2:
        if num%d==0:
            break
        d=d+1
    else:
        count=count+1
        if count==n:
            break
    

    num+=1
print(num)
