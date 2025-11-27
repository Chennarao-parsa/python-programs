#group of words into the anagrams
l=["eat","nat","ate","tae","bat","tan"]
output=[]
for i in l:#eat
    group=[]
    for j in l:#eat,nat
        if sorted(i)==sorted(j):
            group.append(j)

    if group not in output:
        output.append(group)
print(output)
