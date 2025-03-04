#reverse triangle
row=5
#col=5

for i in range(1,row+1):
    for j in range(row):
        if j <  row - i :
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()