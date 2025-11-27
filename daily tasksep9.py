#write a generator to yield all substrings of a given string
'''
def gensub(s):
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            yield s[i:j]
for i in gensub('abc'):
    print(i,end=',')
    '''
#yield unique characters from the string
'''
   
def unique(s):
    s1=''
    for i in s:
        if s.count(i)==1:
            yield i
x=input("enter a string:")
for i in unique(x):
    print(i,end=' ')
    '''
#palindromic numbers upto n
'''
def palindromicno(n):
    for i in range(1,n+1):
        m=str(i)
        if m==m[::-1]:
            n=int(m)
            yield n
n=int(input("enter a number:"))
for i in palindromicno(n):
    print(i,end=' ')
    '''
#write a program for all consonants in a string
'''
def consonant(s):
    for i in s:
        if i not in "aeiouAEIOU" and i.isalpha():
            yield i
s=input("enter a string:")
for i in consonant(s):
    print(i,end=' ')
    '''
#generator that yields  a sliding window over k size
l=[1,2,3,4,5]
def slide(l,k):
   
    for i in range(0,len(l)-(k-1)):
        yield l[i:i+k]
k=int(input("enter a number:"))
for i in slide(l,k):
    print(i)
    



            



