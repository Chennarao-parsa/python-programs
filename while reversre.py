n=int(input("enter  anumber"))
r=0
while n>0:
    remainder=n%10
    r=r*10+remainder
    n=n//10
print("rev of a given number",r)


