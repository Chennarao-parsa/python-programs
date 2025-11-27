rows=int(input("Enter   a no of rows:"))
space=" "
star="*"


for row_no in range(1,rows+1):
    if row_no==1 or row_no==5:
        print(star*rows,sep='')
    else:
        print(star,space*(rows-2),star,sep='')
    
