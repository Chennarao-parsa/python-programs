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
for i in fibonacii(6):
    print(i,end=' ')
    '''
#prime number
def prime(n):
    for i in range(2,n+1):
        for j in range(2,(i//2)+1):
            if i%j==0:
                break
        else:
            yield i
for i in prime(6):
    print(i,end=' ')
            
    
