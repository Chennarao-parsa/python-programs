n1=int(input("enter a number:"))#24
n2=int(input("enter a number2:"))#8
if n1<n2:
    small=n1
else:
    small=n2
d=small
while d>=2:
    if n1%d==0 and n2%d==0:
        print("Gcd is:",d)
        break
    d=d-1
else:
    print("No Gcd")
