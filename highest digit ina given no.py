n=int(input("enter a no"))
n1=0
while n>0:
    digit=n%10
    if digit>n1 :
        n1=digit
    n=n//10
print(n1)
