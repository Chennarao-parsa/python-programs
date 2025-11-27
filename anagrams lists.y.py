#group a list of words into anagrams

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = []

for i in words:
    group = []
    for j in words:
        if sorted(i) == sorted(j):
            group.append(j)
    if group not in output:
        output.append(group)

print(output)
