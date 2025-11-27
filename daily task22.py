#program that takes a string as a input and generates a list where each as a substring
'''
s=input("Enter a string")#vcube
l=[]
for i in range(1,len(s)+1):
    l.append(s[:i])
print(l)
'''

#using fun to find the smallset number
'''
n=int(input("enter a number:"))
def smallest(num):
    small=float('+inf')
    while num>0:
        rem=num%10
        if rem<=small:
            small=rem
        num=num//10
    return small
        

res=smallest(n)
print(res)
'''
#another way
'''
def small_digit(n1):
    if n1<10:
        return n1
    else:
        return min(n1%10,small_digit(n1//10))
        


n=int(input("enter a number:"))
res=small_digit(n)
print(res)
'''
#sum of even digits in a number
'''
def sumofevendigit(num):
    s=0
    while num>0:
        r=num%10
        if r%2==0:
            s=s+r
        num=num//10
    return s
res=sumofevendigit(1788)
print(res)
'''
#write a pyhton program to write the number of words in a sentence
'''

def countwords(st):
    count=0
    m=st.split()
   
    for i in m:
        count=count+1
    return count
res=countwords('python is a powerful language')
print(res)
'''
#given number is a perfect number or not
def perfect(num):
    s=0
    for i in range(1,(num//2)+1):
        if num%i==0:
            s=s+i
    return s
n=int(input("enter a number"))
res=perfect(n)
if res==n:
   print(True)
else:
    print(False)
    
    
                
            
        
    
    
        
    
    
