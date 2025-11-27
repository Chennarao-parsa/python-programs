import random
rand=random.randint(1,100)
print(rand)
d=2
while d<=rand//2:
    if rand%2==0:
        print("not prime")
        break
    d=d+1
else:
    print("prime")
