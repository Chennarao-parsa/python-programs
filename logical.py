#second maximum repeated character in a string
'''
s=input("enter a string:")
d={}
for ch in s:
     d[ch]=s.count(ch)
max1=0
max2=0
char2=''
for ch in d:
     if d[ch]>max1:
          max2=max1
          max1=d[ch]
          char2=''
     elif d[ch]>max2 and d[ch]<max1:
          max2=d[ch]
          char2=char2+ch
     
          
print(char2,max2)
'''
#using the loops and strings
s = 'aabbcccesassss'
s1 = ''
for i in s:
    if i not in s1:
        s1 += i

l1 = []
l2 = []
for i in s1:
    c = 0
    for j in s:
        if j == i:
            c += 1
    l1.append(i)
    l2.append(c)

m1 = float('-inf')
m2 = float('-inf')

for c in l2:
    if c > m1:
        m2 = m1
        m1 = c
    elif m1 > c > m2:
        m2 = c

for i in range(len(l2)):
    if l2[i] == m2:
        print(l1[i], m2)
        break

          
          



     

          
     
