go = True
nt = 0
while go:
    ask = input("\n\t Do you want to create more triangle (yes/no): ")
    if ask.lower() == "no":
        print("\n\t PROGRAM TERMINATED \n","="*100)
        break
        go = False
    else:
        nt += 1
        for x in range(1,5):
            for r in range(1, nt+1):
                for y in range(1,x+1):
                    print("*", end=" ")
                for z in range(5,x,-1):
                    print(" ", end=" ")
                print(end=" ")
            print()
        continue