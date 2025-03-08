from collections import OrderedDict

# Create OrderedDict
od = OrderedDict()
od['apple'] = 2
od['banana'] = 3
od['cherry'] = 1

# Access element
print(od['banana'])

# Update element
od['banana'] = 5

# Pop element
od.pop('apple')

# Move element to end
od.move_to_end('cherry')

# Length
print(len(od))

# Clear
od.clear()

# Comparison
od1 = OrderedDict([('a', 1), ('b', 2)])
od2 = OrderedDict([('a', 1), ('b', 2)])
print(od1 == od2)  # True
