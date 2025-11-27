num=int(input("enter a number"))
n=9
while num>0:
    s=num%10
    if s<n:
        n=s
    num=num//10

print(n)
