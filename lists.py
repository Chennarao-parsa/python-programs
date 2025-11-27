'''# reverse a list
'''
l1=[10,37,67,78,898,788,7,3,33,3,3]
'''
l2=l1[::-1]
print(l2)
'''


    


"""



"""
# duplicates in a given list
'''
# duplicates in a given list

l2=[]
for i in l:
    if i  not in l2:
        l2.append(i)
print(l2)
'''
l=[10,37,67,78,898,788,7,3,33,3,3]
max_value=float('-inf')
min_value=float('+inf')
           
for i in l:
    if i>max_value:
        max_value=i
    if i<min_value:
        min_value=i
print('maximum value is ',max_value,'min value is ',min_value)
