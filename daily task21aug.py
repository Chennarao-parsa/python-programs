#split
'''
s='we are good students'
sa=s.split()
print(sa)
'''
#delem

'''
s='we|are|good|students'
sa=s.split("|")
print(sa)
'''
#only the vowels  from a string
'''
s="programming is fun"
s1=''
for i in s:
    if i in "aeiouAEIOU":
        s1=s1+i
    else:
        pass
print(s1)
        '''
#another
'''
s="programming is fun"
s1=[]
for i in s:
    if i in "aeiouAEIOU":
        s1.append(i)
    
print(' '.join(s1))
'''
'''
#another
s="programming is fun"
vowels=[i for i in s if i in "aeiouAEIOU"]
result=" "+" ".join(vowels)
print(f"'{result}'")
'''
#count how many vowels in agiven string
'''
s="Education is impottant"
c=0
for i in s:
    if i in "aeiouAEIOU":
        c=c+1
print(c)

'''


#reverse a gicen string
'''
s="Python"
m=s[::-1]
print(m)
'''
#vv
'''
s="Python"
m=''

for i in range(len(s)-1,-1,-1):
    m=m+s[i]
print(m)
'''
#palindromes
l=[121,123,454,789,989]
l2=[]
for i in l:
    if str(i)==str(i)[::-1]:
        l2.append(i)
print(l2)
        
        
    
