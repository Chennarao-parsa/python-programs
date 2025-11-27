#longest palindrome substring
'''

s=input("enter a string:")
def palindromesubstring(str):
    big=''
    for i in range(0,len(str)):
        for j in range(len(str),i,-1):
            if str[i:j]==str[i:j][::-1]:
                if len(str[i:j])>len(big):
                    big=str[i:j]
                    break
    return big
res=palindromesubstring(s)
print(res)
            
    
'''
#swap with zero in right side remaining number swap on left side
'''
l=[3,0,2,0,1,0,4,0,51,2]
l2=[]
zero =[]
for i in l:
    if i != 0:
        l2.append(i)
    else:
        zero.append(i)
print(l2+zero)
'''
#unique combination of numbers from a list sum up to agiven target

l = [1, 3, 5, 6, 7, 6, 2]
pairs = []
target = 5
for n in l: 
    if n==target:
        pairs.append((n,))

for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] + l[j] == target:
            pairs.append((l[i], l[j]))
    
print(pairs)

    
