#make multiple triangles

tri = eval(input("\n\t Enter your desired number of triangles: "))
for a in range(1,6):
    for r in range(1,tri+1):
        for b in range(1,a+1):
            print("*",end = " ")
        for c in range(5,a,-1):
            print(" ", end = " ")
        print(end=" ")
    print()