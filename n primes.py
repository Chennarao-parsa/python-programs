n=int(input("Enter a number:"))
count=0
s=0
num=2
while True:
   
  
    for j in  range(2,(num//2)+1):
        if num%j==0:
            break
    else:
        s=s+num
       
        count=count+1
        if count==n:
            break
    num=num+1
print(s)
        

