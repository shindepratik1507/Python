student = {
    "name": "Pratik",
    "age": 21,
    "subjects": {
        "math": 90,
        "science": 85,
        "english": 88
    }
}

print(student)
# Accessing elements
print(student["name"])
print(student["subjects"]["math"])

# Adding elements
student["subjects"]["history"] = 78

# Updating elements
student["age"] = 22

# Removing elements
student["subjects"].pop("science")

# Looping through nested dictionary
for key, value in student.items():
    if isinstance(value, dict):
        print(f"{key} =>")
        for sub_key, sub_value in value.items():
            print(f"   {sub_key} : {sub_value}")
    else:
        print(f"{key} : {value}")
