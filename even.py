sum_even = 0

for i in range(0, 102):  # range goes up to 102 to include 100
    if i % 2 == 0:
        sum_even += i

print("Sum of even numbers between 0 and 101 is:", sum_even)
