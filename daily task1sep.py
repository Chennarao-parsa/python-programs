# create a dictionary from the lists
'''
keys=["a","b","c"]
values=[1,2,4]
d={}
for i  in range(len(keys)):
    d[keys[i]]=values[i]

print(d)
'''
# merge two dictionaries
'''
d1={"a":1}
d2={"b":2,"c":3}
m={}
for k,v in d1.items():
    m[k]=v
for k,v in d2.items():
    m[k]=v
print(m)
'''
'''
a={"a":1}
b={"b":2}
for k in b.keys():
    if k not in a:
        a[k]=b[k]
print(a)
'''
        

# check if key exists in a dictioanry
'''
d={"a":1,"b":2}
k=input("enter a key value: ")
if k in d:
    print(True)
    '''
#iterate over keys and values
'''
d={"a":10,"b":20}
for k,v in d.items():
    print(k,v)
'''
#sum of values in a dictionary
'''
d={"a":19,"b":20}
s=0
for v in d.keys():
    s=s+d[v]
print(s)
'''
#python program to remove a key from the dictionary
d={"a":1,"b":2}
print(d)
k=input("enter a key to remove")
d.pop(k)
print(d)

    
