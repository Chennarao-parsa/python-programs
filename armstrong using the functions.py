def digitcount(n):
    d_cnt=0
    while n>0:
        n=n//10
        d_cnt+=1
    return d_cnt

def sumofdigitpowers(n,p):
    s=0
    while n>0:
        t=n%10
        s=s+t**p
        n=n//10
    return s
def is_armstrong(n):
    cnt=digitcount(n)
    sum=sumofdigitpowers(n,cnt)
    if sum==n:
        print(n,"is an armstrong number")
    else:
        print(n,"not armstrong number")
res=is_armstrong(1563)
