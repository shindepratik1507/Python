from collections import ChainMap

# Create dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Create ChainMap
cm = ChainMap(dict1, dict2)

# Access values
print(cm['a'])  # 1
print(cm['c'])  # 3

# Update value
cm['a'] = 10

# Add new dictionary
cm = cm.new_child({'e': 5})

# Remove value
cm.pop('a')

# Get keys and values
print(list(cm.keys()))   # ['e', 'b', 'c', 'd']
print(list(cm.values())) # [5, 2, 3, 4]

# Reverse order
rev_cm = ChainMap(*reversed(cm.maps))
print(rev_cm)
