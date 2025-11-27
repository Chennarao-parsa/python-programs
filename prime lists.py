l = [2,3, 4, 7, 9, 11, 13, 15]

for i in l:
    if i > 1:  # primes are greater than 1
        for j in range(2, (i//2)+1):
            if i % j == 0:  # if divisible by any number other than 1 and itself
                break
        else:
            print(i)  # this runs if loop didn't break → prime
