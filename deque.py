#deque

from collections import deque

# Create deque
d = deque([10, 20, 30])

# Add elements
d.append(40)
d.appendleft(5)

# Remove elements
d.pop()
d.popleft()

# Extend
d.extend([50, 60])
d.extendleft([0, -10])

# Rotate
d.rotate(2)
d.rotate(-1)

# Remove specific element
d.remove(20)

# Display final deque
print(d)
