
'''=int(input("enter a number:"))
i=1
while i<=n:
    j=1
    while j<=n-1+1:
        if i==1 or i==n:
            print(chr(64+j),end='')
        else:
            print(chr(64+j)," "*(n-2),chr(64+i))
        j=j+1
        print()
    i=i+1 print(ch + ' ' * (2 * n - 3) + ch)
    '''
   
n = 5
i = 1
while i<=n:
    
    if i == 1 or i == n:
        print((chr(64+i)+" ")*n)
        
    else:
       
        print(chr(64+i)+" "*(2*n-3)+chr(64+i))
    i += 1     
