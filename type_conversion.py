#type conversion
x=10, name=pratik
a=str(x)+ name #int to string
print(a)

# Convert int to float
x = 5      # int
y = float(x)  

print(y)       # 5.0
print(type(y)) # <class 'float'>

# Convert float to int (decimal part removed)
a = 3.75
b = int(a)   

print(b)       # 3
print(type(b)) # <class 'int'>


# Convert string to int
# Convert string to float
x = "25"
y = int(x)   
z = float(x) 

print(y)       # 25
print(z)       # 25.0



# List to Tuple
list1 = [1, 2, 3]
tuple1 = tuple(list1)

# Tuple to List
tuple2 = (4, 5, 6)
list2 = list(tuple2)

print(tuple1) # (1, 2, 3)
print(list2)  # [4, 5, 6]


