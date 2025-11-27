'''
s='apple is a fruit and orange too'
m=s.split()
l=[]
for i in m :
    if i[0] in "aeiouAEIOU":
        l.append(i)
print(l)
'''
#reverse the list of strings
'''
l=["vcube","python","java"]
l.reverse()
l2=[]
for i in l:
    m=i[::-1]
    l2.append(m)
print(l2)
    '''
#string is palindrome or not
'''
s=input("enter a string:")
if s==s[::-1]:
    print("string is palindrome")
    '''
#flatten a deeply nested list that may contain multiple data types like tuples,lists,and sets.
'''
l=[1,2,3,(4,5),[6,7],8,9]
flat=[]
for i in l:
    if isinstance(i,(list,tuple,set)):
        flat.extend(i)
    else:
        flat.append(i)
print(flat)
'''
#write a python program to sort a list of tuples based on their first index(second ele) in a each tupple
'''
l = [(1,3), (2,1), (4,5), (3,2)]

for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i][1] > l[j][1]:
            l[i], l[j] = l[j], l[i]

print(l)
'''


    
        
        
    
        
