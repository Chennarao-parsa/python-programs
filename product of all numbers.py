#product of all digits in a number
'''
n=int(input("enter a number:"))
def productnum(num):
    p=1
    while num>0:
        
        r=num%10
        p=p*r
        num=num//10
    return p
res=productnum(n)
print(res)
'''
#number of factors of a given number
'''
n=int(input("enter  a number:"))
def factors(num):
    c=0
    while num>0:
        for i in range(1,num+1):
            if num%i==0:
                c=c+1
        return c
res=factors(n)
print(res)

'''
#sum of even digits in a number
'''
n=int(input("enter a number:"))
def evendigits(num):
    ed=0
    while num>0:
        n=str(num)
        for i in n:
            if int(i)%2==0:
                ed=ed+int(i)
        return ed

res=evendigits(n)
print(res)
'''
#count the number of vowels and consonents in a string
'''
s=input("enter a string:")
def vcstr(str):
    vc=0
    cc=0
    for i in str:
        if i.isalpha():
            if i in "AEIOUaeiou":
                vc=vc+1
            else:
                cc=cc+1
    return vc,cc
vc,cc=vcstr(s)
print("vowels",vc)
print("consonants",cc)
'''
#armstrong number
def dcount(num):
    count=0
    while num>0:
        count=count+1
        num=num//10
    return count
def sum_of_digits(num):
    count=dcount(num)
    s=0
    bkp=0
    while num>0:
        t=num%10
        s=s+t**count
        num=num//10
    return s
def is_arm(num):
        


