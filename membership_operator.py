#membership operator
#IN,NOT IN
#IN
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)  # True
print("orange" in fruits)  # False

text = "Hello World"
print("H" in text)  # True
print("Z" in text)  # False

#NOT IN
fruits = ["apple", "banana", "cherry"]
print("orange" not in fruits)  # True
print("apple" not in fruits)   # False

text = "Hello World"
print("Z" not in text)  # True
print("H" not in text)  # False
