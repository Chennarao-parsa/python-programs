'''
l=[1,2,3,2,1]
y=[]
for i in l:
    y=[i]+y
if l==y:
    print("True")
else:
    print("false")
    '''
# second largest in a list
"""
l=[1,24,56,78,34]
largest=float("-inf")
second_lar=float("-inf")
for i in l:
    if i>largest:
        second_lar=largest
        largest=i
    if i>second_lar and i<largest:
        second_lar=i
print(second_lar)
"""
# Common elements  between  two lists

l1=[1,2,3]
l2=[2,3,4]
for i in l1:
    
    if i in l2:
        print(i)
'''
l=[1,2,3]
for i in range(len(l)):
    print(i)
'''
