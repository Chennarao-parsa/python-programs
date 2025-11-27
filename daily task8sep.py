#generator  fibonacci
'''def fibonacii(n):
    a=0
    b=1
    yield a
    yield b
    for i in range(n-2):
        c=a+b
        yield c
        a=b
        b=c
for i in fibonacii(n):
    print(i,end=' ')
    '''
#prime number
'''
n=int(input("enter a number:"))
def prime(n):
    for i in range(2,n+1):
        for j in range(2,(i//2)+1):
            if i%j==0:
                break
        else:
            yield i
for i in prime(n):
    print(i,end=' ')
    '''
#factorial of number staring from  1 to n
'''
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        yield fact
for i in fact(5):
    print(i,end=' ')
        '''
#write a generator fun to yield only vowels from a string.
'''
def vowel(s):
    for i in s:
        if i in "aeiouAEIOU":
            yield i
for i in vowel("education"):
    print(i,end=' ')
    '''
#perfect squares

def perfect(n):
    for i in range(1,n+1):
        res=int(i**0.5)
        if res*res==i:
            yield i
for i in perfect(30):
    print(i,end=' ')
            
    
