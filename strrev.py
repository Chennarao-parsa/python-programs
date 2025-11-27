str=input("enter a string")
rev=""
i=len(str)-1
while i>0:
    rev=rev+str[i]
    i=i-1
print("rev of a string",rev)
