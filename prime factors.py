#prime factors for a fgiven number
'''

num=int(input("enter a number:"))
l=[]
for d in range(2,(num//2+1)):
    if num%d==0:
        for i in range(2,(d//2)+1):
            if d%i==0:
                break
        else:
            l.append(d)
print(l)
'''
# another
num=int(input("enter a number:"))
l=[]
for d in range(2,num+1):
    while num%d==0:
        l.append(d)
        num//=d
print(l)
    
        
            
