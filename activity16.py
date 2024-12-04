#make an inverted triangle

for a in range(-1,5):
    for b in range(-1, a+1):
        print(" ", end=" ")
    for c in range(5, a, -1):
        print("*", end=" ")
    for d in range(4, a, -1):
        print("*", end=" ")
    print()
  