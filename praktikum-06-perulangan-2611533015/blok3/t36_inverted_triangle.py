height = int(input("Height: "))

for row in range (height, 0, -1):
    for column in range(1, row + 1):
        print("*", end="")
    print()