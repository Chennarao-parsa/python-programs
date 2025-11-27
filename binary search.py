x = [1, 23, 333, 33, 5, 43, 3323]
x.sort() 
print("Sorted list:", x)

ele = int(input("Enter an element you want to find: "))

s = 0
e = len(x) - 1


while s <= e:
    m = (s + e) // 2
    if x[m] == ele:
        print("Element found at index:", m)
        found = True
        break
    elif ele > x[m]:
        s = m + 1
    else:  
        e = m - 1

else:
    print("not found")
