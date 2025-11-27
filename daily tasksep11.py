#removing the duplicates characters from a given string while preserving the order of first occurences
def dup(str):
    s1=''
    for ch in str:
        if ch not in s1:
            s1+=ch
    return s1
print(dup("programming"))

#Neon number or not
'''
num=int(input("enter a number:"))
s=num**2
sum=0
while s>0:
    r=s%10
    sum=sum+r
    s=s//10
if num==sum:
    print("Neon")
else:
    print("not a Neon")
    '''
#return all unique pairs of numbers from  list
'''
l=[1,3,2,2,4,0,5]
target=4
l2=[]
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==target:
            l2.append((l[i],l[j]))
print(l2)
'''
#using decorator count the number vowels in the output of a function
'''
def countvowels(f):
    def innerfun():
        output=f()
        c=0
        for i in output:
            if i in "aeiouAEIOU":
                c=c+1
        return c
    return innerfun
@countvowels   
def display():
    s="Decorator Example"
    return s
res=display()
print(res)
'''
#yields elements of  a list until  a negative number is found
'''
l=[5,7,9,-1,4]
def gen(lis):
    for i in lis:
        if i>0:
            yield i
        else:
            break
for i in gen(l):
    print(i,end=' ')
    '''
    

            
