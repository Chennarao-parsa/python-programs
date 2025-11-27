rows=int(input("enter number of rows:"))
space=" "
star="*"
for row_no in range(1,rows+1):
    if row_no==1 or row_no==5:
        print(star*row_no,sep='')
    else:
        print(star,space*(row_no-1),star,sep='')
