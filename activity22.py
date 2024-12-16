# #Creating your own python function
# def panghello():
#     print("="*100, "\n\t Hello dear IT1A")
# for n in range(1,11):
#     panghello()

def activity1():
    print("Hello World")
def activity2():
    num1 = eval(input("\n Please input a number: "))
    num2 = eval(input("\n Please input another number: "))

    print(num1, "Floor divided to", num2, "=", num1 // num2 )
def activity3():
    full_name = input("\n\n\t\t\t\t\t Bio-Data \n\n\t Please type your Name: ")
    gender = input("\t Please type your Gender: ")
    age = input("\t Please type your Age: ")
    BDate = input("\t Please type your Date of Birth: ")
    BPlace = input("\t Please type your Birth Place: ")
    Height = input("\t Please type your Height(ft): ")
    Weight = input("\t Please type your Weight(kg): ")
    Btype = input("\t Please type your Blood Type: ")

    StrtAd = input("\t Please type your Street name: ")
    Sub_CompAd = input("\t Please type your Subdivision/Compound/Village: ")
    Brgy = input("\t Please type your Barangay name: ")
    CitAd = input("\t Please type your City Name: ")
    ProvAd = input("\t Please type your Provincial Name: ")
    Zip = input("\t Please type your Zip Code: ")
    CvStatus = input("\t Please type your Civil Status: ")
    Nat = input("\t Please type your Nationality: ")
    Rel = input("\t Please type your Religion: ")

    LgKnown = input("\t Please type your Language/s known: ")
    Hobby = input("\t Please type at least 2 Hobbies related to IT: ")
    Sk = input("\t Please type your 3 Skills: ")

    EDetails = input("\n\t\t\t\t EDUCATIONAL BACKGROUND ")
    ESch = input("\n\t Please type your Elementary School name: ")
    HSch = input("\t Please type your High School name: ")
    Col = input("\t Please type your College School name: ")
    Cou = input("\t Please type your Chosen Course: ")
    Sec = input("\t Please type your Section's name: ")

    FBg = input("\n\t\t\t\t FAMILY DETAILS")
    Fn = input("\t Father's name: ")
    Fcn = input("\t Contact No.: ") 
    Mn = input("\t Mother's name: ")
    Mcn = input("\t Contact No.: ")

    CtD = input("\n\t\t\t\t CONTACT DETAILS ")
    ConDe = input("\t Contact No.: ")
    ConD = input("\t E-mail Address: ")

    print("\n\n\n\n\t\t\t\t Hi, I am" , full_name, gender , "and I am" , age , "years old. I was born on" , BDate , "at" , BPlace, ". \n\t I am" , Height , "tall and weighs", Weight , "with a blood type of" , Btype , ". I live in", StrtAd, Brgy, CitAd, "," , Zip, ", in" , ProvAd , ". \n\t My status is \t" , CvStatus , ", and i'm a" , Nat , "and is a " , Rel , ". I know" , LgKnown , "and my hobbies are" , Hobby , "while my \n\t skills are" , Sk , ". \n\t\t\t I finished my primary education at" , ESch , ", while my secondary education happened at" , HSch , ". \n\t I'm currently studying at" , Col, "with a course" , Cou , ", in section", Sec , ". \n\t My father is" , Fn , "and my mother is" , Mn, ".  You can contact me with my cellphone number," , ConDe , "and an e-mail of \n\t" , ConD,"." )

def activity4():
    print("\n\t =====================================================")

    num1 = eval(input("\n Enter a number: "))
    num2 = eval(input("\n Enter another number: "))

    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    flr_div = num1 // num2
    exp = num1 ** num2
    mod = num1 % num2

    print("\n\t The sum of", num1, "and", num2, "is", add, "\b.\n\t The difference of", num1, "and", 
        num2, "is", sub, "\b.\n\t The product of", num1, "and", num2, "is", mul, "\b.\n\t The quotient of", 
        num1, "and", num2, "is", div, "\b.\n\t The floor division of", num1, "and", num2, "is", flr_div, "\b.\n\t", 
        num1, "exponent by", num2, "is", exp, "\b.\n\t The remainder of", num1, "and", num2, "is", mod)

def activity5():
    print("\n\t =====================================================")
    fahrenheit = eval(input("\n\t Enter temperature in Fahrenheit: "))
    celsius = ((fahrenheit - 32) * 5) /9

    print("\n\t", fahrenheit, "degrees Fahrenheit converted to celsius is", celsius, "degrees or")
    print(f"\t {fahrenheit} degrees Fahrenheit converted to celsius is {round(celsius, 2)} degrees")


while True:
    print("="*100, "\n\t Activity \t  1  \t  2 \t  3 \t  4 \t  5 \t  Exit")
    ask = input("\n\t Hi dear user. Please select an activity that you want to view: ")
    if ask.lower() == "1":
        activity1()
    elif ask.lower() == "2":
        activity2()
    elif ask.lower() == "3":
        activity3()
    elif ask.lower() == "4":
        activity4()
    elif ask.lower() == "5":
        activity5()
    elif ask.lower() == "exit":
        print("\n\t Thank you for viewing this program ^w^")
        break
    else:
        print("\n\t Please select a number from the activities.")
        continue