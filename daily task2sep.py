# string into a dictionary of a characters
'''
s=input("enter  a string:")#banana
d={}
for i in s:
    d[i]=s.count(i)
print(d)
    '''
#dictionary with  keys and their squares
'''
l=[1,2,3]
d={}
for i in l:
    d[i]=i*i
print(d)
'''
#frequency count of the words
'''
s=input("enter  a sentence:")
m=s.split()
d={}
for i in m:
    d[i]=m.count(i)
print(d)
'''
#invert keys and values in a dictionary

a={"a":1,"b":2}
k=list(a.keys())
v=list(a.values())
d={}
for i in range(0,len(v)):
    d[v[i]]=k[i]
print(d)

#check if two dictionaries are equal
'''
a={"a":1}
b={"a":1}
if a==b:
    print(True)
    '''
