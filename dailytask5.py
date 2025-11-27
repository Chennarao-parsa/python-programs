#sum of values in adictionary
'''
d={'a':10,'b':20}
s=0
for v in d.values():
    s=s+v
print(s)
#or
d={'a':10,'b':20}
s=sum(d.values())
print(s)
'''
#add a key value pair or update if the key already existed
'''
d={'name': 'Alice', 'age': 25}
d['age']=30
print(d)
'''
#determine the number of key value pairs in a dictionary
'''
d={'name':'Alice','age':25}
c=0
for k,v in d.items():
   c=c+1
print(c)
#or
d={'name':'Alice','age':25}
m=len(d)
print(m)
'''
#sort the dictionary by its values
d = {'a': 3, 'b': 1, 'c': 2}
sorted_dict = {}
d_copy = d.copy()
while d_copy:
    min_key = None
    min_value = float('inf')
    for k, v in d_copy.items():
        if v < min_value:
            min_value = v
            min_key = k
    sorted_dict[min_key] = min_value
    d_copy.pop(min_key)

print(sorted_dict)  # {'b': 1, 'c': 2, 'a': 3}
# max value key
d = {'x': 20, 'y': 40, 'z': 10}

max_key = None
max_value = float('-inf')  # start with very small value

for k, v in d.items():
    if v > max_value:
        max_value = v
        max_key = k

print(max_key)   # y


    

