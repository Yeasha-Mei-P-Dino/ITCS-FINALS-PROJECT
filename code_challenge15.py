#PACKAGE
# HYBRID LOOP
import os 
name = input("\n\t Hello, dear user! What's your name? ")
tri = input("\n\t Well, do you want to see a triangle (yes/no): ")
if tri.lower() == "yes":
    print("\n\n")
    for x in range(1,6):
        for y in range(6, x, -1):
            print(" ", end =" ")

        for z in range(x, 0,-1):
            print("*", end =" ")
    
        for a in range(2, x+1):
            print("*", end =" ")
        print()
else:
    print("\n\t Eh di don't.")
    
con = True
num = 0
while con == True:
    ask = input("\n\t Do you want to CREATE a triangle (yes/no): ")
    if ask.lower() == "yes":
        os.system('cls')
        num += 1
        for x in range(1,5):
            for y in range(1,num + 1):
                for z in range(1,x+1):
                    print("*", end=" ")
                for a in range(5, x, -1):
                    print(" ", end=" ")
            print()
        continue

    elif ask.lower() == "no":
        print(f"\n\t Thanks for participating {name}. The total amount of triangle you made is {num}.")
        print("\n\t Program terminated...")
        print("."*130)
        break
        con == False

    else:
        os.system('cls')
        print("\n\t You entered an invalid answer. TRY AGAIN.")
        print("."*100)
        continue
    