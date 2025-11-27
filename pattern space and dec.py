rows=int(input("enter a nnumber:"))
space=' '
row_no=1
star='*'
while row_no<=rows:
    print(space*(rows-row_no),star*(row_no))
    row_no=row_no+1
