n=int(input("enter a number:"))
start=1
for i in range(1,n+1):
    num=start

    for j in range(i):
        print(num,end=' ')
        num=num+2
        
    print()
    start=start+i
    
