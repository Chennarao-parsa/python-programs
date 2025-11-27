def traverse_array(arr):
    n = len(arr)
    print("Traversing array in small steps:")
    for i in range(n):
        print(f"Step {i+1}: at index {i}, value = {arr[i]}")
    print("Reached the last element:", arr[-1])


# Example usage
arr = [14, 24, 45, 67, 56, 44, 32, 23]
traverse_array(arr)
