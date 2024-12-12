#continue to ask a number then provide the sum 
import os 

print("\n\n\t Ooohh...")
name = input("\t Hi dear user! What's your name? ")


isGo = True
sum = 0
while isGo == True:
    num = eval(input("\n\t Enter a number -> "))
    sum += num 
    if (num <= 10 and num >= 0) :
        if num == 0:
            print("\n\t Yey! The loop has been terminated.")
            con = input("\n\t Would you still like to continue giving numbers(yes/no):")
            if con.lower() == "no":
                os.system("cls")
                print(f"\n\t Dear {name}, the number you entered has a total of {sum}.")
                print("\n\t Program stopped.","."*100)
                break
                isGo == False 

            else:
                os.system("cls")
                print("\n\t So you want more ^o^?")
                continue
        else:
            continue
        
    else:
        print(f"\n\t You typed an invalid number, {name}. TRY AGAIN.")
        print("."*128)
        continue
         

