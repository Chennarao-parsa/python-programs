import random
fix=random.randint(1,9)
i=1
while i<=3:
    guess=int(input("Guess number:"))
    if guess==fix:
        print("You won the game:")
    else:
        print("wromg Guess:")

    i+=1
else:
    print("you lost the Game")
print("game over")
