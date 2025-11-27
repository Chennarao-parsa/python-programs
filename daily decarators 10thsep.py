#decarator that prints "function  started " before and "function ended " after a function runs
''''def decfun(fun):
    def innerfun():
        print("Function started")
        fun()
        print("Function ended")
    return innerfun
@decfun     
def func():
    print("Hello!")
func()
'''
#converts a output of a function into the lowercase
'''
def lowersec(f):
    def innerfun():
        output=f()
        return output.lower()
    return innerfun
@lowersec

def lower():
    s="ALICE"
    return s
res=lower()
print(res)
'''
#converts into uppercase
'''
def upperdec(f):
    def innerfun():
        output=f()
        return output
    return innerfun
@upperdec
def upper():
    s="vcube"
    return s
res=upper()
print(res)
'''
#def execution time
'''
def exe(f):
    def innerfun():
        import time
        start=time.time()
        output=f()
        end=time.time()
        yield output
        print("Execution time",end-start)
    return innerfun
@exe
def time():
    s="Task completed"
    return s
for i in time():
    print(i)
'''
#capital letters to small and small to capital
def deccapsmall(f):
    def innerfun():
        string=f()
        output=''
        
        for i in string:
            if i.isupper():
                output+=i.lower()
            else:
                output+=i.upper()
        yield output
    return innerfun
@deccapsmall
def capsmall():
    s='HeLLO PyThon WorLD'
    return s
for i in capsmall():
    print(i)
    
