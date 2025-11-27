'''#prime no between 1 to 100
i = 2  # start from 2, since 1 is not a prime number

while i <= 100:
    c = 0  # count of factors

    j = 1
    while j <= i:
        if i % j == 0:
            c = c + 1
        j = j + 1

    if c == 2:
        print(i, end='\n')  # print prime number
    elif c>2:
        print("composite")
    else:
        print("0")

    i = i + 1
    '''

          
n = int(input("Enter a number: "))
i = 2
count = 0

while i <= n :
    if n % i == 0:
        count += 1
    i += 1

if count > 2:
    print(n, "is a composite number")
else:
    print(n, "is not a composite number")
