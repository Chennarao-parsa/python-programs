
rows=int(input("enter a number:"))
space=" "
star="*"
row_no=1
while row_no<=rows:
    print(space*(rows-row_no),star*(2*row_no-1))
    row_no=row_no+1
    
