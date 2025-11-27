x=[20,47,67,78,8,60,15]
first_min =float('+inf')
second_min=float('+inf')
for i in x:
    if i<first_min:#20<+inf
       
        second_min=first_min
        first_min=i
    if i<second_min and i>first_min:
        secon_min=i
print(second_min)
        
   
        

        
