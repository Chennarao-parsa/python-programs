n=int(input("enter the number of rows:"))

for r in range(n,0,-1):
    for i in range(1,n+1):
        print(" "*(r-1),chr(64+i)," "*(i-1),end="",sep='')
      
    print()
           
