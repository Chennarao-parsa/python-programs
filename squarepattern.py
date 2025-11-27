n=int(input("ENter a  no of rows:"))
i=1
while i<=n:
    j=1
    while j<=(n-i+1):
        if i==1 or i==n:
            print(chr(64+i),end='',sep=" ")
        else:
            print(chr(64+i)," "*(i-2),chr(64+i))
            j=j+1
    i=i+1
    print()
    
            

'''        rows=int(input("Enter   a no of rows:"))
space=" "
star="*"

for row_no in range(1,rows+1):
    if row_no==1 or row_no==5:
        print(star*rows,sep='')
    else:
        print(star,space*(rows-2),star,sep='')
    '''
