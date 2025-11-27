#decimal to roman
roman=['X','IX','V','IV','I']
decimal=[10,9,5,4,1]
n=int(input("enter a number:"))#17
for d in decimal:
    q=n//d
    if q>0:
        id=decimal.index(d)
        print(roman[id]*q,end='')
        n=n%d
        
        
    
