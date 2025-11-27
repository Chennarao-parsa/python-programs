n1=int(input("enter a num"))
n2=int(input("enter anumber"))
if n1%2==0 and n2%2==0:
    print(n1+n2)
elif (n1%2==0 and n2%2!=0) or (n1%2!=0 and n2%2==0):
    print(n1-n2)
else:
    print(n1*n2)
