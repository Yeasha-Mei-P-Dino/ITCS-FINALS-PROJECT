#not a sharp diamond
#arrow up

print("\n\n")
for x in range(1,6):
    for y in range(6, x, -1):
        print(" ", end =" ")

    for z in range(1, x+1):
        print("*", end =" ")
    
    for a in range(1, x+1):
        print("*", end =" ")

    print()


#arrow down
for x in range(1,6):
    for y in range(1, x+1):
        print(" ", end =" ")

    for z in range(6, x, -1):
        print("*", end =" ")
    
    for a in range(6, x, -1):
        print("*", end =" ")

    print()

print("\n\n")