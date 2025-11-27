s=input("enter a string")
def wordcount(st):
    r=s.split()
    print(r)
    return len(r)
res=wordcount(s)
print(res)
