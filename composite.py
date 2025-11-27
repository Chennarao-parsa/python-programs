n = int(input("Enter a number: "))
i = 2
count = 0

while i <= n // 2:
    if n % i == 0:
        count += 1
        break
    i += 1

if count > 0:
    print(n, "is a composite number")
else:
    print(n, "is not a composite number")
