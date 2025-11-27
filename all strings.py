#strings
#string reverse
'''
s="students"
print(s[::-1])
'''
#extracting the characters
'''
s="students"
for i in s:
    print(i)
    '''
#strings into the upper without using upper method
'''
s="STudents"
def uppercase(st):
    output=''
    for i in st:
        a=ord(i)
        if a>=97 and a<=122:
            output=output+chr(a-32)
        else:
            output=output+i
    return output
res=uppercase(s)
print(res)
'''
#using upper method
'''
s="students"
m=s.upper()
print(m)
'''
#1 to 100 how many 2's are there
'''
def numcount(start,end):
    cnt=0
    for i in range(start,end+1):
        cnt=cnt+str(i).count('2')
    return cnt
res=numcount(1,100)
print(res)
'''
#splitting the string
'''
s="we are good students"
st=s.split()
print(st)
'''
#splitting the string using the delimeter as given list
s=("we are|good,students-hi")
def splitstring(st):
    delimiter=['|',',','-',' ']
    word=''
    output=[]
    for ch in st:
        if ch in delimiter:
            if word:
                output.append(word)
                word=''
        else:
            word=word+ch
    else:
        if word:
            output.append(word)
    return output
res=splitstring(s)
print(res)
    
