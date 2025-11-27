
numbers=[10000,1000,100,90,80,70,60,50,40,30,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
words=["ten thousand","thousand","hundred","ninety","eighty","seventy","sixty","fifty","forty","thirty","twenty","nineteen","eighteen","seventeen","sixteen","fifteen","fourteen","thirteen","twelve","eleven","ten","nine","eight","seven","six","five","four","three","two","one"]
n=int(input("Enter a number:"))
for d in numbers:
    if d==10000 or d==1000 or d==100:
        q=n//d
        if q>0:
            q_idx=numbers.index(q)
            d_idx=numbers.index(d)
            
            print(words[q_idx],words[d_idx],"and",end=' ')
            n=n%d
    else:
        q=n//d
        if q>0:
            d_idx=numbers.index(d)
            print(words[d_idx],end=' ')
            n=n%d
        
    
'''
numbers=[10000,1000,100,90,80,70,60,50,40,30,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
words=["ten thousand","thousand","hundred","ninety","eighty","seventy","sixty","fifty","forty","thirty","twenty","nineteen","eighteen","seventeen","sixteen","fifteen","fourteen","thirteen","twelve","eleven","ten","nine","eight","seven","six","five","four","three","two","one"]

n=int(input("Enter a number: "))

for d, w in zip(numbers, words):
    q=n//d
    if q>0:
        if d >= 100:   # handle thousand, hundred, etc.
            print(words[numbers.index(q)], w, end=' ')
        else:
            print(w, end=' ')
        n=n%d
'''
