#sorting the dictionary based on the values
d={'a':5,'b':2,'c':9,'d':1}
l=list(d.items())
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i][1]>l[j][1]:
            l[i],l[j]=l[j],l[i]

d=dict(l)
print(d)
