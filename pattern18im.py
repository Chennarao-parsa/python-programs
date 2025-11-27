n=int(input("Enter a no of rows:"))
space=' '
star='*'
for i in range(1,n+1):
    if i==1 or i==n:
        print(space*(i-1),star*(n-i+1),sep='')
    else:
        print(space*(i-1),star,space*(n-i-1),star,sep='')
