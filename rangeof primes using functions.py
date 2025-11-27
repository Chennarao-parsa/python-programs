def isprime(n):
    if n<2:
        return False
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    else:
        return True
def rangeprime(s,e):
    for n in range(s,e+1):
       if isprime(n):
           print(n,end=' ')
rangeprime(1,100)
