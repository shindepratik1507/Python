hash_table = {
    "name": "Pratik",
    "age": 21,
    "city": "Pune"
}

# Adding element
hash_table["country"] = "India"

# Updating element
hash_table["age"] = 22

# Removing element
hash_table.pop("city")

# Looping through elements
for key, value in hash_table.items():
    print(f"{key} => {value}")

# Nested hash table
hash_table["subjects"] = {"math": 90, "science": 85}

# Checking existence of a key
if "name" in hash_table:
    print("Name exists")

print(hash_table)
