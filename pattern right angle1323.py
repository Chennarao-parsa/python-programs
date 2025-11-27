rows=int(input("enter number of rows:"))
space=" "
star="*"
for row_no in range(rows+1):
    if row_no==1:
        print(star*rows)
    elif row_no==6:
        print(space*row_no,star)
    else:
        print(space*(row_no-1),star,space*(rows-(row_no-1)),star)
        
    
