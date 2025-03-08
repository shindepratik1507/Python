import array

# Creating an array
arr = array.array('i', [1, 2, 3, 4, 5])

# Accessing elements
print(arr[0])  # 1

# Adding elements
arr.append(6)
arr.insert(2, 10)

# Removing elements
arr.pop(1)
arr.remove(10)

# Slicing
print(arr[1:4])  # [3, 4, 5]

# Updating
arr[0] = 100

# Looping through array
for num in arr:
    print(num)

# Concatenation
arr2 = array.array('i', [7, 8])
result = arr + arr2

# Length
print(len(result))
