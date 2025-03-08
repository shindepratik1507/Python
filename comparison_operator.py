#comparison operator
x = 10
y = 5

print(x == y)  # False (10 is not equal to 5)
print(x != y)  # True  (10 is not equal to 5)
print(x > y)   # True  (10 is greater than 5)
print(x < y)   # False (10 is not less than 5)
print(x >= y)  # True  (10 is greater than or equal to 5)
print(x <= y)  # False (10 is not less than or equal to 5)

#string
name1 = "Apple"
name2 = "Banana"

print(name1 == name2)  # False
print(name1 != name2)  # True
print(name1 < name2)   # True ('Apple' comes before 'Banana')
print(name1 > name2)   # False

#tuple
list1 = [1, 2, 3]
list2 = [1, 2, 4]

print(list1 == list2)  # False
print(list1 < list2)   # True (comparison happens at 3 vs 4)


#if-else
x = 20
y = 15

if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")


#loop
i = 1

while i <= 5:
    print(i)
    i += 1
