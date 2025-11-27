#selection sort
x=[4,44,45,78,9,22]
for i in range(len(x)-1):
    min_value=min(x[i:])
    idx=x.index(min_value)
    x[i],x[idx]=x[idx],x[i]
print(x)
