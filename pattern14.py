
n = int(input("Enter number of rows: "))
i = 1
while i <=n:
    print(" " * (i-1), end='')  
    j = 1
    while j <= (n - i+1):
        print(chr(64+ j), end=' ')
        j += 1
    print()
    i += 1
