#bubble sort

x=[1,2,37,89,9]
for i in range(0,len(x)):
    for j in range(0,len(x)-i-1):
               if x[j]>x[j+1]:
                   x[j],x[j+1]=x[j+1],x[j]
print(x)

