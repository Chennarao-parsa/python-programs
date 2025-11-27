#second largest
'''
x=[14,24,45,67,56,44,32,23]
f=float('-inf')
s=float('-inf')
for i in x:
    if i>f:
        s=f
        f=i
    if i>s and i<f:
        s=i
print(s)

'''
#second min
x=[14,24,45,67,56,44,32,23]
s=float('+inf')
s1=float('+inf')
for i in x:
    if i<s:
        s1=s
        s=i
    elif i < s1 and i != s:
        s1=i
print(s1)
'''

text = "apple,banana,cherry"

print(text.split(','))  # sep=','
# Output: ['apple', 'banana', 'cherry']

text2 = "one  two   three"
print(text2.split())    # sep=None (default)
# Output: ['one', 'two', 'three']

print(text2.split(' ')) # sep=' ' (exact space)
# Output: ['one', '', 'two', '', '', 'three']

'''
