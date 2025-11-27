
#count of characters
'''s=input("enter a string:")
uc=0
lc=0
dc=0
ssc=0
for ch in s:
    if ch.isupper():
        uc+=1
    elif ch.islower():
        lc+=1
    elif ch.isdigit():
        dc+=1
    else:
        ssc+=1
print("upprer:",uc)
print("lower:",lc)
print("digit count:",dc)
print("SP",ssc)'''

#lonhgest substring without repeating characters
'''

s = input("enter a string:")

def longest_unique_substring(text):
    big = ""
    for i in range(len(text)):
        sub = ""
        for j in range(i, len(text)):
            if text[j] in sub:   # repeated char → stop
                break
            sub += text[j]
            if len(sub) > len(big):
                big = sub
    return big

res = longest_unique_substring(s)
print(res)
'''
#non repeating characters as longest substriong
'''
s=("abcabcbb")
output=''
for ch in s:
    if ch not in output:
        output=output+ch
print(output)
'''
#repaeted characters with char followed by the number of times
'''
s='aaabbbccc'
s1=''
for ch in s:
    if ch not in s1:
        s1=s1+(ch+str(s.count(ch)))
print(s1)
'''
#group a list of words into anagrams

l=["eat","tea","tan","ate","nat","bat"]
output=[]
for i in l:
    if i not in vis:
        
        l1=[]
        for j in l:
            if sorted(i)== soretd(j):
                l1.append(j)
    if i not in l:
        output.append(l1)
print(output)
            
l = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = []
visited = set()   # to avoid duplicates

for i in l:
    if i not in visited:
        l1 = []
        for j in l:
            if sorted(i) == sorted(j):
                l1.append(j)
                visited.add(j)
        output.append(l1)

print(output)

    
            
            
    
    
