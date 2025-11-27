# Password is a strong or not
'''

p=input("enter a password:")
u,l,d,s=0,0,0,0
for i in p:
    if i.isupper():
        u=1
    elif i.islower():
        l=1
    elif i.isdigit():
        d=1
    elif i.isalnum()==False:
        s=1
if len(p)>=8 and u>=1 and l>=1 and d>=1 and s>=1:
    print("strong")
else:
    print("Not strong")

        
'''
#To  find the first charsacter that doesnot repeat anywhere
'''
s=input("Enter a string")
for i in s:
    if s.count(i)==1:
        print(i)
        break
'''
#python Program to rewmove the all punctuation marks in a given string
'''
s=input("Enter a string:")
output=''
for i in s:
    if 65<=ord(i)<=90 or 97<=ord(i)<=122 or i in "9876543210" or i==' ':
        output=output+i
print(output)
'''
#count jow many upper and lower case letters,numbers,And symblos
'''        
p=input("enter a string:")
u,l,d,s=0,0,0,0
for i in p:
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
    elif i.isdigit():
        d+=1
    elif i.isalnum()==False:
        s+=1
print("upper",u)
print("lower",l)
print("digit",d)
print("symbol",s)
'''
#longest word in a given sentence
'''
s="Python is a powerful language"
m=s.split()
longest=''
length=0
for i in m:
    if len(i)>length:
        length=len(i)
        longest=i
print(longest)
'''
#vowels in a list
'''
s="programming is fun"
s1=''
for i in s:0
    if i in "aeiouAEIOU":
        s1=s1+i
print(s1)
'''
'''
s="programming is fun"
s1=[]
for i in s:
    if i in "aeiouAEIOU":
        s1.append(i)
    
print(' '.join(s1))
'''
#sort only integers in a list and non-integers remain same
x=[30,"py",50,80,30,"jy"]
y=[]
for i in x:
    if type(i)==int:
        y.append(i)
y.sort()
for j in range(0,len(x)):
    if type(x[j])!=int:
            y.insert(j,x[j])
print(y)
        
