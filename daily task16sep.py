#factorial of a number using recursive functions
'''
#fact
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5))
'''
#sum of natural numbers
'''
def sumofnatural(n):
    if n==1:
        return 1
    return n+sumofnatural(n-1)
print(sumofnatural(10))
'''
#reverse a string using the functions
def revstr(s):
    if len(s)<=1:
        return s
    else:
        return revstr(s[1:])+s[0]
print(revstr("hello"))


#nth term of the fibonacii series
'''
def fibonacii(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibonacii(n-1)+fibonacii(n-2)
n=int(input("enter a number:"))
for i in range(n):
    print(fibonacii(i),end=' ')
    '''

    
    
