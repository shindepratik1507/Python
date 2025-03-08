from collections import namedtuple

# Define a NamedTupl
Person = namedtuple('Person', ['name', 'age', 'city'])

# Create an instance
p1 = Person(name="Pratik", age=22, city="Pune")
p2 = Person(name="Dipak", age=20, city="Pune")

# Access values
print(p1.name)  # Pratik
print(p1.age)   # 22
print(p1.city)  # Pune

print(p2.name)  
print(p2.age)   
print(p2.city)
