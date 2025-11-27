fobj=open('D://primenumbers.txt','w')
if fobj.writable():
    for num in range(2,10001):
        for d in range(2,(num//2)+1):
            if num%d==0:
                break
        else:
            fobj.write(str(num)+'\n')
fobj.close()
        
