# find all primes from a list using functions
'''
def isprime(num):
    if num<2:
        return False
    for n in range(2,(num//2)+1):
        if num%n==0:
            return False
    return True
l=[2,3,4,5,6,7,8,9,10,11]
l2=[]
for i in l:
    
    if isprime(i):
        l2.append(i)
print(l2)

#all primes betweeen 1 to 100

def prime(s,e):
    for i in range(s,e+1):
        
        for d in range(2,(i//2)+1):
            if i%d==0:
                break
        else:2004
            print(i)
prime(1,100)
'''

# armstrong number using functions
'''
def digitcount(num):
    d_cnt=0
    while num>0:
        num=num//10
        d_cnt+=1
    return d_cnt
def sumofdigitpowers(num,p):
    s=0
    while num>0:
       
        t=num%10
        s=s+t**p
        num=num//10
    return s
def isarmstrong(num):
    cnt=digitcount(num)
    s=sumofdigitpowers(num,cnt)
    if s==num:
        return True
    else:
        return False
res=isarmstrong(152)
print(res)
res=digitcount(152)
print(res)
res=sumofdigitpowers(152,3)
print(res)
'''
# n th prime number
n=int(input("enter a number:"))
cnt=0
s=0
num=2
while True:
    for j in range(2,(num//2)+1):
        if num%j==0:
            break
    else:
        s=s+num
        cnt=cnt+1
        
        if cnt==n:
            break
    num=num+1
print(num)
print(s)

    




























    
                
