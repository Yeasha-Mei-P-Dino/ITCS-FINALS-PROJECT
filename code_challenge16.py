# make a Banking account that can deposit and withdraw 
# breakdown a Filipino denomination that will only be terminated if the user choose to stop it

go = True
bal = 5000 
initial_dep = 2000
def greet():
    print("\n\t\t\t\t\t\t Plumeria Bank \n\t Good day!")
    print("\n\t SELECT TRANSACTION   \n\n\t 1 - Check Balance   \t\t\t\t 2 - Deposit Cash")
    print("\t 3 - Withdraw Cash   \t\t\t\t 4 - Pay Bills \n\t 5 - Create an Account \t\t\t\t 6 - Exit \n")

def exit():
    print("\nThank you for using our bank. The system will now close. \n","_"*120)
def bal_amt():
    print(f"\nYour current balance is {bal}.")
def in_dep():
    print(f"\nYour initial deposit is {initial_dep}.")
def receipt2():
    rec = input("\n Do you need to print a receipt? ")
    if rec.lower() == "yes":
        print("="*120)
        print(f"\n\t\t\t\t\t\t Plumeria Bank \n\t TRANSACTION \n\t Cash Withdrawal \n\n\t AMOUNT: {amt} \n\t Balance: {bal} \n", "="*120)
    elif rec.lower() == "no":
        exit()
    else:
        print("You've entered an invalid answer.")
def receipt1():
    rec = input("\nDo you need to print a receipt? ")
    if rec.lower() == "yes":
        print("="*120)
        print(f"\n\t\t\t\t\t\t Plumeria Bank \n\t TRANSACTION \n\t Cash Deposit \n\n\t AMOUNT: {dep} \n\t Balance: {bal} \n\t Initial deposit: {initial_dep} \n", "="*120)
    elif rec.lower() == "no":
        exit()
    else:
        print("You've entered an invalid answer.")
def mon():
    print("\n\t PHP 1,000 \t PHP 2,000 \t PHP 5,000 \t PHP 10,000 \t Other amount")
def nm():
    name = input("\n Enter your name: ")
    pin = input("\n Enter your pin number: ")
def denomi1():
    ans1 = dep_2 // 1000 
    num1 = dep_2 % 1000
    ans2 = num1 // 500
    num2 = num1 % 500
    ans3 = num2 // 200
    num3 = num2 % 200
    ans4 = num3 // 100
    num4 = num3 % 100
    ans5 = num4 // 50
    num5 = num4 % 50
    ans6 = num5 // 20
    num6 = num5 % 20
    ans7 = num6 // 10
    num7 = num6 % 10
    ans8 = num7 // 5
    num8 = num7 % 5
    ans9 = num8 // 1
    print(f"\n\t Current Balance: \n\t 1000 - {ans1} \n\t 500 - {ans2} \n\t 200 - {ans3} \n\t 100 - {ans4}")
    print(f"\t 50 - {ans5} \n\t 20 - {ans6} \n\t 10 - {ans7} \n\t 5 - {ans8} \n\t 1 - {ans9}")
    receipt1()
    exit()
def denomi2():
    ans1 = amt_2 // 1000 
    num1 = amt_2 % 1000
    ans2 = num1 // 500
    num2 = num1 % 500
    ans3 = num2 // 200
    num3 = num2 % 200
    ans4 = num3 // 100
    num4 = num3 % 100
    ans5 = num4 // 50
    num5 = num4 % 50
    ans6 = num5 // 20
    num6 = num5 % 20
    ans7 = num6 // 10
    num7 = num6 % 10
    ans8 = num7 // 5
    num8 = num7 % 5
    ans9 = num8 // 1
    print(f"\n\t Current Balance: \n\t 1000 - {ans1} \n\t 500 - {ans2} \n\t 200 - {ans3} \n\t 100 - {ans4}")
    print(f"\t 50 - {ans5} \n\t 20 - {ans6} \n\t 10 - {ans7} \n\t 5 - {ans8} \n\t 1 - {ans9}")
    receipt2()
    exit()


while go:
    greet()
    choose = input("Please select an option: ")
    if choose == "1":
        nm()
        bal_amt()
        exit()
        continue
    elif choose == "2":
        nm()
        in_dep()
        mon()
        dep = int(input("\nPlease select the amount that you want to deposit: "))
        dep_2 = dep + bal 
        print(f"Your current balance is {dep_2}")
        denomi1()
    elif choose == "3":
        nm()
        in_dep()
        mon()
        amt = int(input("Select an amount that you want to withdraw: "))
        if amt <= 4500:
            amt_2 = bal - amt
            print(f"Your remaining cash is now {amt_2}.")
            denomi2()
        else:
            print(f"Your current balance is only {bal}. Try again")
            continue
    elif choose.lower() == "4":
        nm()
        print("\n\n\n\t Sorry, this program is still under observation. Please try our other options... \n", "."*120)
        exit()
        continue
    elif choose == "5":
        acc = input("Enter your name: ")
        pn = input("Enter a pin: ")
        print("Account created.")
        exit()
        continue
    elif choose == "6":
        exit()
        break
    else:
        continue
