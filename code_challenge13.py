
# sharp diamond but with numbers
#arrow up

print("\n\n")
for x in range(1,6):
    for y in range(6, x, -1):
        print(" ", end =" ")

    for z in range(x, 0,-1):
        print(z, end =" ")
    
    for a in range(2, x+1):
        print(a, end =" ")
    print()

#arrow down
for b in range(4, 0, -1):
    for c in range(6, b,-1):
        print(" ", end =" ")

    for d in range(b, 0,-1):
        print(d, end =" ")
    
    for e in range(2, b+1):
        print(e, end =" ")
    print()

print("\n\n")