# revers a list
'''l=[10,20,30,40,50]
y=[]
for i in l:
    y=[i]+y
print(y)
'''
#remove all occurence of a specified value

n=int(input("enter a no:"))
l=[1,2,4,4,5]
for i in l:
    if i==n:
        while n in l:
            l.remove(i)
print(l)

