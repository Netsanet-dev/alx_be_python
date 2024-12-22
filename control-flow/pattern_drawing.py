pattern = int(input("Enter the size of the pattern: "))
row = 0
while pattern > row:
    for i in range(pattern):
        print("*", end="")
    print()
    row += 1
