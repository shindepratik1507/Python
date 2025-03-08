#nested loop
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print(' ')

#pattern print
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print('*', end=' ')
    print()
