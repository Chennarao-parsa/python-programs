#using the join method
'''
x=["vcube","python","java","ml"]
output='-'.join(x)
print(output)
'''
#without the join method
'''
x=["vcube","python","java","ml"]
output=''
for i in range(0,len(x)):
    if i==len(x)-1:
        output=output+x[i]
    else:
        output=output+x[i]+'-'
print(output)
'''
#replace one word with another
'''
s="we are learning python are are"
output=s.replace("are","o")
print(output)
'''
#Formatted string
s='my friend is {} and his IS {}'
output=s.format('raju',36)
print(output)



