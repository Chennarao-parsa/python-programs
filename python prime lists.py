l=[1,2,23,4,7,9]
for n in l:
    if n>1:
    
        for i in range(2,n):
            if n%i==0:
                break
            
        else:
            print(n)
           


            
