#sets
'''
s={True,10,"hi","hello",20}
print(s)
'''
#adding an element
'''
s={True,10,"hi","hello",20}
s.add(30)
print(s)
'''
#REmoving an element
'''
s={True,10,"hi","hello",20}
s.remove(20)
print(s)
'''
#if you remove the item which is not in the set it throws error in the set
'''s={True,10,"hi","hello",20}
s.remove(33)
print(s)
'''
#discard
#it doesn't throw error even if you give the ele not in set
'''
s={True,10,"hi","hello",20}
s.discard(33)
print(s)
'''
#set theory operations
#union
'''
s1={True,10,"hi","hello",20}
s2={90,"python",1}
output=s1.union(s2)
print(output)
#print(s1 | s2)'''
#intersection
'''
s1={True,10,"hi","hlisten
ello",20}
s2={90,"python",1}
output=s1.intersection(s2)
#print(s1 & s2)
print(output)
'''
#difference
'''
raju
s1={True,10,"hi","hello",20}
s2={90,"python",1}
output=s1.difference(s2)
print(output)
output=s2.difference(s1)
print(output)
'''
#symmetric difference
'''
s1={True,10,"hi","hello",20}
s2={90,"python",1}
output=s1.symmetric_difference(s2)
print(output)
'''
# example
'''
t={'p1','p2','p3'}
e={'p4','p3','p5'}
print("only one news paper every day",t^e)
print("atleast one news paper",t|e)
print("only english paper",e-t)

print("both news papers ",t&e)
'''
#Anagram
'''
s1=input("enter a string:")
s2=input("enter another string:"
s1=set(s1)
s2=set(s2)
if len(s1^s2)==0:
    print("anagram")
else:
    print("not a anagrm")
    '''
#heterogram
'''
s=input("enter a string")
if len(set(s))==len(s):
    print("heterogram")
else:
    print("not a heterogram")
    #or
    '''
'''
s=input("enter a string")
for i in s:
    if s.count(i)>1:
        print("not a heterogram")
        break
else:
    
    print("heterogtram")
    '''
#methods
#pop()-removes last ele
'''
s={10,20,"vcube",True,"python"}
res=s.pop()
print(res)
print(s)
'''
#if a set contains the numbers it removes the least number in the set
'''
s={10,89,57,78,89,343,1}
res=s.pop()
print(res)
print(s)
'''
#update method
'''
x={10,"vcube","python",True}
y={20,"python",1}
x.update(y)
print(x)
'''
#clear
'''
x={10,"vcube","python",True}
x.clear()
print(x)
'''
#copy
'''
x={10,"vcube","python",True}
y=x.copy()
print(x)
print(y)
'''
#set comprehension
'''
x={i for i in range(1,11) if i%2==0}
print(x)
'''
#create A EMPTY set
'''
s=set()
m=set()
s.add(1)
m.add(1)
print(m)
#n=s.remove(1)

#print(n)
print(s)
'''
#check if one set is a subset of another
'''
s1={1,2,3,4,5}
s2={1,2,3,4,5,6,7}
print(s1.issubset(s2))
print(s2.issuperset(s1))
'''
#if two sets are disjoint
'''
s1={1,2,3,4,5}
s2={7,8}
print(s1.isdisjoint(s2))
'''
#find the max in a set and also min
'''
s1={1,2,3,4,5}
m=max(s1)
n=min(s1)
print("MAXIMUM ele is",m)
print("mimimum ele is",n)
'''
#convert list into  A set
'''
l=[21,4,5,55]
print(set(l))
'''
#remove an ele in a set if exists otherwise do nothing
'''
s1={1,2,3,4,5}
s1.discard(6)
print(s1)
'''
'''
s1={1,2,3,4,5}
ele=int(input("enter  a number:"))
for ch in s1:
    if ch==ele:
        s1.remove(ch)
        break
print(s1)
'''

#create a frozenset in pyhton
'''
s1=frozenset({1,2,3,4,5})
print(s1)
'''
#check if a set is empty without using len()
'''

s=()
if not s:
    print("empty")
else:
    print("not empty")
    '''
#update a set with the ele from a another set
'''
s1={1,2,3,4,5}
s2={3,5,67,8}
s1.update(s2)
print(s1)
'''
#remove and return the arbitary ele from a set
''' some error
s1={1,2,3,4,5}
s2=()
print(type(s2))
s2=s1.pop()
print(s2)
print(type(s2))
print(s1)
'''
s1={1,2,3,4,5}


   
