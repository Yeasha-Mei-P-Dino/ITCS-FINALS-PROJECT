#Python Demo for NESTED CONDITION
#Data Filtration Program

name = input("\n\t Enter your name: ")
isStudent = input("\n\t Are you a current student of DLL (yes/no): ")

if isStudent.lower() == "yes":
    print("\n\t What year are you currently enrolled? \n\t F - Freshmen \n\t S - Sophomore \n\t J - Junior \n\t R - Senior ")
    yearLevel = input("\n\t Please enter your answer here:  ")
    if yearLevel.lower() == "f":
        print(f"\n\t Hi {name}, our dear freshmen. Welcome to DLL ^w^")
    elif yearLevel.lower() == "s":
        print(f"\n\t Hi {name}, our dear sophomore. Welcome to DLL ^w^")
    elif yearLevel.lower() == "j":
        print(f"\n\t Hi {name}, one of our junior. Welcome to DLL ^w^")
    elif yearLevel.lower() == "r":
        print(f"\n\t Hi {name}, one of our senior. Welcome to DLL ^w^")
    else:
        print("\n\t You've entered a different answer. Try again.")
else:
    print("Thank you for using the system.")
