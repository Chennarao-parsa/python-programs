#find all palindroms from a list using functions
'''
l=['madam','hello','noon','python']
output=[]
def palindrome(str):
    for i in l:
        if i==i[::-1]:
            output.append(i)
    return output
res=palindrome(l)
print(output)
'''
#python program to find the shortest word in  a sentence
'''
s=input("Enter a string")

def shortestword(str):
    shortest=float("+inf")
    m=s.split()
    small=''
    for i in m:
        if len(i)<shortest:
            shortest=len(i)
            small=i
    return small            
        

res=shortestword(s)
print(res)
'''
#Python program to find the longest palindrome string using functions
'''
s=input("enter a string")
def palindrome(string):
    m=string.split()
    z=[]
    for i in m:
        if i==i[::-1]:
            z.append(i)
    return z
def longestpalin(string):
    z=palindrome(string)
    large=''
    max_len=0
    for i in z:
        if len(i)>max_len:
            max_len=len(i)
            large=i
    return large
res=palindrome(s)
print(res)
res=longestpalin(s)
print(res)
            '''
#tuple
'''
t=(1,2,3,4,5)
a,*b,c=t
print(a,b,c)
'''
#ex
'''
a=(1,2)
b=[5,3]
c=a+tuple(b)
print(c)
'''
#strings
'''
s="abc"
s[0]="A"
print(s)

'''
#program
''''
a,b=(1,2,3)[0:2]
print(a,b)
'''
#list
x=([1,2],)
x[0].append(3)
print(x)
