# sorting dictionary keys based on their based on their key length

d={'abc':1,'a':2,'ab':3}
l1=list(d.items())
for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        if len(l1[i][0])>len(l1[j][0]):
            l1[i],l1[j]=l1[j],l1[i]
d=dict(l1)
print(d)

#key with longest value

'''
d={'a':'hi','b':'hello','c':'hey'}
l1=list(d.items())
length=0
d=''
for i in range(len(l1)):
    if len(l1[i][1])>length:
        length=len(l1[i][1])
        d=l1[i][0]
print(d)
'''
    
#program to map each character in a given string to a list of all positions  indices where the character appers
'''
s='banana'
d={}
for i in range(len(s)):
    if s[i] in d:
        d[s[i]].append(i)
    else:
        d[s[i]]=[i]
print(d)
'''

