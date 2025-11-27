rows=int(input("enter roowws :"))
middle=(rows//2)+1
space=" "
star="*"
row_no=1
while row_no<=rows:
    if row_no<=middle:
        print(space*(middle-row_no),sta/' 9r,space*(row_no-1),star*(2*row_no-1))
        row_no=row_no+1
    else:
        pass
