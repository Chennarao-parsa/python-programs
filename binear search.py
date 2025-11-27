x=[1,2,3,4,5,6,7,8]
ele=int(input("Enter a element:"))#3
s=0
e=len(x)-1
while True:
    m=(s+e)//2
    if x[m]==ele:
        print("found")
        break
    elif s>e:
        print("false")
        break
    elif ele>x[m]:
        s=m+1
    elif ele<x[m]:
        e=m-1
    else:
        pass
        
        
        
    
