from collections import defaultdict

# Default value as int
d = defaultdict(int)

# Adding values
d['apple'] += 2
d['banana'] += 3

# Looping through defaultdict
for key, value in d.items():
    print(key, value)

# Using lambda for default value
d = defaultdict(lambda: "Not Found")
print(d['mango'])

# Nested defaultdict
nested_dict = defaultdict(lambda: defaultdict(int))
nested_dict['fruits']['apple'] = 5

# Frequency count
data = ['apple', 'banana', 'apple', 'cherry', 'banana']
count = defaultdict(int)
for fruit in data:
    count[fruit] += 1

print(count)
