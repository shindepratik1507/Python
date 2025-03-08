from collections import Counter

# Create counter
counter = Counter('apple')

# Access elements
print(counter['p'])

# Update counter
counter.update('banana')

# Subtract elements
counter.subtract('apple')

# Get most common
print(counter.most_common(2))

# Remove zero or negative counts
counter = +counter

# Arithmetic operations
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
print(c1 + c2)  # Addition

# Convert to dictionary
print(dict(counter))
