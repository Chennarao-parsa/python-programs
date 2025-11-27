# decimal to roman
roman=['X','IX','V','IV','I']
decimal=[10,9,5,4,1]
n=int(input('entet a number you want to convert:'))
for i in decimal:
    q=n//i
    if q>0:
        idx=decimal.index(i)
        print(roman[idx]*q,end='')
        n=n%i
