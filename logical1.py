
# it affects the original list
'''
x=[1,2,3]
y=x
y.extend([4,5])
print(x)
print(y)
'''

#it does not effects the original list
'''
x=[1,2,3]
y=x
y=y+[4,5]
print(x)
'''
#
x=[1,2]
y=[x]*2
y[0][0]=10
print(y)
print(y[0][0]+y[1][0])
