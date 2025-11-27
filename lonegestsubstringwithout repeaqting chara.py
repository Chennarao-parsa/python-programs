'''def longestsub(s):#abcabbcc
    longest=''
    for i in range(len(s)):
        sub=''
        for j in range(i,len(s)):
            if s[j] in sub:
                break
            sub=sub+s[j]
            if len(sub)>len(longest):
                longest=sub
    return longest
s=input("enter a string:")
res=longestsub(s)
print(res)
'''
#longest palindrome substring
'''
def longestpalindrome(s):
    long=''
    for i in range(len(s)):
        for j in range(len(s),i,-1):
            if s[i:j]==s[i:j][::-1]:
                if len(s[i:j])>len(long):
                    long=s[i:j]
    return long
s=input("enter a string:")
print("longest palindrome sunstring is:",longestpalindrome(s))
'''
#sum of even digits in  a number #123456
'''
def sumofevendigits(n):
    s=0
    while n>0:
        r=n%10
        if r%2==0:
            s=s+r
        n=n//10
    return s
print("even digits of a number is:",sumofevendigits(1234556))
'''
# sum of the even indexes of a given numer
def evenindexsum(n):#12435687
    st=str(n)
    s=0
    for i in range(0,len(st),2):
        s=s+int(st[i])
    return s
print("sum of even indexes in a number is",evenindexsum(12435687))
