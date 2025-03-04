#diamond pattern
row = 5

#upper part
for i in range(1,row + 1):
    for j in range(row - i):
        print(" ",end=" ")

    for k in range(2 * i - 1):
            print("*",end=" ")
    print()

#lower part
for i in range(row, 0, -1):
    for j in range(row - i):
        print(" ",end=" ")

    for k in range(2 * i - 1):
            print("*",end=" ")
    print()