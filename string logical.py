s='1a2b3c4d'
s1=''
for ch in s:
    if not ch.isdigit():
        s1=s1+ch*2
print(s1)
