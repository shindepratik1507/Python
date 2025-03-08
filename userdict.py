from collections import UserDict

class MyDict(UserDict):
    def __setitem__(self, key, value):
        print(f"Setting {key} = {value}")
        super().__setitem__(key, value)
    
    def __getitem__(self, key):
        print(f"Getting value of {key}")
        return super().__getitem__(key)

    def __delitem__(self, key):
        print(f"Deleting {key}")
        super().__delitem__(key)

d = MyDict()
d['apple'] = 10
d['banana'] = 20
print(d['apple'])
del d['apple']
print(d)
