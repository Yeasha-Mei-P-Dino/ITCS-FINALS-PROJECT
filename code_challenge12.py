# make an arrow pointing upward

print("\n\n")
for x in range(1,5):
    for y in range(5, x, -1):
        print(" ", end =" ")

    for z in range(1, x+1):
        print("*", end =" ")
    
    for a in range(1, x+1):
        print("*", end =" ")

    print()

for x in range(1,5):
    for y in range(5, 4, -1):
        print(" ", end = "\t")

    for z in range(5, 4, -1):
        print("* *", end = " ")

    print()

print("\n\n")