x=[1,2,3,4,5,6,7,8,9]
for i in x:
    if i>1:
        for  j in range(2,(i//2)+1):
            if i%j==0:
                break
        else:
            print(i)
