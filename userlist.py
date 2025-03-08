from collections import UserList

class MyList(UserList):
    def __setitem__(self, index, value):
        print(f"Setting value at index {index} = {value}")
        super().__setitem__(index, value)
    
    def __getitem__(self, index):
        print(f"Getting value at index {index}")
        return super().__getitem__(index)

    def __delitem__(self, index):
        print(f"Deleting value at index {index}")
        super().__delitem__(index)

l = MyList([10, 20, 30])
l[1] = 50
print(l[1])
del l[1]
print(l)
