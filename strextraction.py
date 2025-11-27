s="hello world"
l=[]
l1=[]
for i in range(len(s)):
    if s[i]=='l':
        l.append(i)
        l1.append(s[i])
print(l,l1, sep="\n")
