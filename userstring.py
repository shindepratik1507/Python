from collections import UserString

class MyString(UserString):
    def upper(self):
        return self.data.upper()
    
    def lower(self):
        return self.data.lower()
    
    def add_suffix(self, suffix):
        return self.data + suffix
    
    def format_string(self):
        return f"** {self.data} **"
    
    def starts_with(self, prefix):
        return self.data.startswith(prefix)

s = MyString("Hello, World")
print(s.upper())                   # Output: HELLO, WORLD
print(s.lower())                   # Output: hello, world
print(s.add_suffix("!!"))          # Output: Hello, World!!
print(s.format_string())           # Output: ** Hello, World **
print(s.starts_with("Hello"))      # Output: True
print(s.starts_with("Python"))     # Output: False
