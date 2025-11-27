import random
n=random.randint(1,20)


i=1
while i<=3:
    guess=int(input("enter your guess:"))
    
    if guess==n:
        print("your guess is correct")
        break
    elif guess<n:
        print("your guess is low:")
    else:
        print("your guess is too high")
    
    i=i+1
else:
    print("you lost and corret no is",n)
print("game over")
