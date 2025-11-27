n=int# Fibonacci series using while loop
n = int(input("Enter how many terms you want: "))

a = 0  # First term
b = 1  # Second term
count = 0

print("Fibonacci Series:")
while count < n:
    print(a, end=' ')
    c = a + b
    a = b
    b = c
    count += 1
