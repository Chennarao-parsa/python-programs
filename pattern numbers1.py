rows=int(input("Enter  a number:"))
space=" "
row_no=1
while row_no<=rows:
    print(space*(row_no-1),end='')
    i=1
    while i<=rows-row_no+1:
        print(i,end='')
        i=i+1
        j=rows-row_no
    while j>=1:
        print(j,end='')
        j=j-1
        
    print()
    row_no=row_no+1
