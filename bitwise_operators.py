#bitwise operators
a = 12  # 1100 (Binary)
b = 10  # 1010 (Binary)

print("AND: ", a & b)  # 1000 -> 8
print("OR: ", a | b)   # 1110 -> 14
print("XOR: ", a ^ b)  # 0110 -> 6
print("NOT a: ", ~a)   # -13
print("Left Shift a << 1: ", a << 1)  # 11000 -> 24
print("Right Shift a >> 1: ", a >> 1) # 0110 -> 6

a = 5
b = 3

if (a & b) > 0:  #(&,|,^,~,<<,>>)
    print("AND is non-zero")
else:
    print("AND is zero")
