# Python program to find all pairs whose sum is equal to the k i.e target
'''
l=[1,3,2,2,4,5]
t_sum=5
pairs=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==t_sum:
            pair=(min(l[i],l[j]),max(l[i],l[j]))
            if pair not in pairs:
                  pairs.append(pair)
            
print(pairs[1],pairs[0])
'''
#program to find the how many characters in a string
'''
s=input("enter string:")
cnt=0
for ch in s:
    cnt=cnt+1
print(cnt)
    
print(len(s))
'''
#program to find the how many characters in a string but donot count space
'''

s=input("enter string:")
cnt=0
for ch in s:
    if ch==' ':
        continue
    cnt=cnt+1
print(cnt)
'''
#lowercase to upper
'''
s=input()
def upperprogram(st):
    output=''
    for i in st:
        n=ord(i)
  
        if n>=97 and n<=122:
            output=output+chr(n-32)
        else:
            output=output+i
    return output

res=upperprogram(s)
print(res)
'''
#program to find sort elements in alist as int and nonint
'''
l=[30,"py",50,80,"jy",20]
l2=[]
l3=[]
for i in l:
    
    if str(i).isdigit():
        l2.append(int(i))
    else:
        l3.append(i)
l2.sort()
result=[]
j=0
for i in l:
    if str(i).isdigit():
        result.append(l2[j])
        j+=1
    else:
        result.append(i)
print(result)
'''
#program to find vowel or consonant
'''
s=input()
for i in s:
    if i.isalpha():
        if i in "aeiouAEIOU":
            print(i,"vowel")
        else:
            print(i,"consonent")
    else:
        print(i,"not a vowel consonant")
        '''
#Sum of digits in a string using functions
'''

s=input("enter a string:")
def sumofdigit(st):
    s1=0
    for i in st:
       
        if i.isdigit():
            s1=s1+int(i)
     
    return s1
            
    

res=sumofdigit(s)
print(res)
'''
#count how many 2 are there for a particular range
'''
def dcountfun(start,end):
    cnt=0
    for i in range(start,end+1):
        cnt=cnt+str(i).count('2')
    return cnt
        

res=dcountfun(1,100)
print(res)

'''
#biggest palindrome substring
'''
s=input()
def palindrome(srt):
    big=''
    for i in range(0,len(srt)):
        for j in range(len(srt),i,-1):
            if srt[i:j]==srt[i:j][::-1]:
                if len(srt[i:j])>len(big):
                    big=srt[i:j]
                break
    return big
res=palindrome(s)
print(res)
'''

#palimdrome smallest palindrome sub str
s=input()
def palindrome(str):
    small=None
    for i in range(0,len(str)):
        for j in range(len(str),i,-1):
            if str[i:j]==str[i:j][::-1]:
                if len(str[i:j])>1:
                    
                    if small is None or len(str[i:j])<len(small):
                        small=str[i:j]             
    return small
res=palindrome(s)
print(res)
            
    
