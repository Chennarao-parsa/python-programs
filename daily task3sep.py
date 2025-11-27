#list comprehension
'''
l=[1,2,3,4,5]
l=[i*2  if i%2==1 else i for i in range(1,6)]
print(l)
'''
#pyhthon program to find the longest word in a sentence that is a palindrome
'''
s=input("enter a string:")
str=s.split()


def longestpalindrome(str):
    big=''
    for i in str:
        if i==i[::-1]:
            if len(i)>len(big):
                big=i
    return big
res=longestpalindrome(str)
print(res)
'''
#merge two dictionaries using update method
''''
d1={"a":1}
d2={"b":2}
d3=d1.copy()
d3.update(d2)
print(d3)
#or
d1={"a":1}
d2={"b":2}
d3={**d1,**d2}
print(d3)
'''
#retrieve a value from a dictioanry without raising an error
'''
d={"name":"alice"}
print(d.get("age"))
print(d.get("name"))
'''
#To get the TOp N highest values from a dictionary
data = {'a': 10, 'b': 50, 'c': 30}
N =int(input("enter a number:"))

result = []
d = data.copy()   

for _ in range(N):
    max_key = None
    max_value = float('-inf')
    for k, v in d.items():
        if v > max_value:
            max_value = v
            max_key = k
    result.append((max_key, max_value))
    d.pop(max_key)

print(result)   # [('b', 50), ('c', 30)]


