    
#create a  empty dictionary and value
'''
d={}
d['a']=1
print(d)
'''
#Accessing values associated with a  specific key
'''
d={"a":1,"b":2,"c":3}
k=input("enter a key:")
if k in d:
    for i in d.keys():
        if i==k:
            print(d[i])
            '''
#Adding a key value pair or updating  if the key exists
'''
d={"a":1,"b":2,"c":3}
d["v"]=4
print(d)
'''
#remove the key value pair from the dictionary
'''
d={"a":1,"b":2,"c":3}
res=d.pop('b')
print(res)
print(d)
'''
#set default method- returns the value of the key if the key exists
'''
d={"a":1,"b":2,"c":3}
print(d.setdefault("a",10))
print(d.setdefault("d",30))
print(d)
'''
#update method
'''
d={"a":1,"b":2,"c":3}
e={"d":5,"e":5,"f":6}
d.update(e)
print(d)
print(e)
'''
#dictionary comprehension
'''
output={}
for i in range(1,11):
    output[i]=i
print(output)
'''
'''
output={i:i for i in range(1,11)}
print(output)   
'''
#sorting
'''
x={'z':4,'y':0,'a':10,'b':3}
y=list(x.items())
for i in range(len(y)):
    for j in range(i+1,len(y)):
        if y[i][0]>y[j][0]:
            y[i],y[j]=y[j],y[i]
      
y=dict(y)
print(y)
'''
    
#group a list of words into anagrams

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = []

for i in words:
    group = []
    for j in words:
        if sorted(i) == sorted(j):
            group.append(j)
    if group not in output:
        output.append(group)

print(output)

            
