roman=['L','XL','X','IX','V','IV','I']
decimal=[50,40,10,9,5,4,1]
num=int(input("ENter a number:"))
for d in decimal:
    q=num//d
    if q>0:
        idx=decimal.index(d)
        print(roman[idx]*q,end='')
        num=num%d
        
        
        
        
