#Compilation of all the lessons in ITCS102 
#Without import of code challenges
import os
import time

os.system('cls')    # Clear screen and start loading process
time.sleep(1) 
print("\t\t\t\t\t\t\t\t Loading. ")
for m in range(1,5):    # First loading step 
    os.system('cls')
    print("\t\t\t\t\t\t\t\tLoading.")
    print('\t\t\t\t\t\t\t████')
    os.system('cls')
    print("\t\t\t\t\t\t\t\tLoading..")
    print('\t\t\t\t\t\t\t███████████')
    os.system('cls')
    print("\t\t\t\t\t\t\t\tLoading...")
    print('\t\t\t\t\t\t\t█████████████████████')
    time.sleep(1)  
os.system('cls')
name = input("\n\t Greetings! Welcome to Mei's Program. Please state your name: ")
print(f"\n\t Hello {name}, I will now show you the contents of this program. \n\t", "="*100)

def tops():
    print('\n\t Topics 1-14: \n\t 1. PRINT STATEMENTS \n\t 2. ESCAPE SEQUENCE \n\t 3. ARITHMETIC OPERATORS')
    print('\t 4. ASSIGNMENT OPERATORS \n\t 5. RELATIONAL OPERATORS \n\t 6. LOGICAL OPERATORS \n\t 7. CONDITIONAL STATEMENTS')
    print('\t 8. LOOPING STATEMENT: FOR LOOP \n\t 9. WHILE LOOP \n\t 10. FUNCTION')
    print('\t 11. FUNCTION w/ RETURN STATEMENT \n\t 12. DOCUMENTATION STRING \n\t 13. MODULE \n\t 14. LIST')

def tops2():
    print('\n\t Topics 1-9: \n\t 1a. PRINT STATEMENTS \n\t 2a. ESCAPE SEQUENCE \n\t 3a. ARITHMETIC OPERATORS')
    print('\t 4a. ASSIGNMENT OPERATORS \n\t 5a. RELATIONAL OPERATORS \n\t 6a. LOGICAL OPERATORS \n\t 7a. CONDITIONAL STATEMENTS')
    print('\t 8a. LOOPING STATEMENT: FOR LOOP \n\t 9a. WHILE LOOP ')
          
def objective():
    """\t To provide learners with a comprehensive understanding of basic Python programs and its concepts."""
def manage():
    """\t Click/type the certain words/numbers to view the information as well as to make the code user-friendly. \n
      Learning to code is learning to create and innovate so enjoy the process! \(OwO)/"""

def question():
    qq =  input("\n\t If you have questions you can just type: h = help(objective) or hm = help(manage): ")
    if qq.lower() == "h":
        help(objective)
    elif qq.lower() == "hm":
        help(manage)
    else:
        print("\n\t Okieee, enjooyy ^w^")

def add():
    print("\n\t 1a - Dictionary \t\t 2b - Tuple \t\t\t 3c - Error handling")
    print("\t 4d - History \t\t\t 5e - Variables \t\t 6f - Operators")
    print("\t 7g - Data types \t\t 8h - Control flow \t\t 9i- Input/Output")
    que = input("\n\t Choose a topic that you want to know: ")
    if que == "1a":
        flower_dict= { 1: 'Rose', 2: 'Tulip', 3: "Sunflower", 4: "Daisy", 5: "Lily"}
        print(f"\n\t To print/show, (flower_dict[1]) {flower_dict[1]}")
        print("\n\t To add a name of flower, you'll just type my_flowers.add_flower(1, Rose)")
        print("\n\t To access it, type my_flowers.get_flower(2) ")
        print("\n\t To delete my_flowers.delete_flower(2)") 
        print("\n\t To display all, type my_flowers.display_flowers()")
    elif que == "2b":
        tuple = (10, 20, 30, 40, 50)
        print("\n\t", tuple)
        print("\n\t Tuple is like a list but it cannot be changed when created. ")

    elif que == "3c":
        print("\n\t This part is about Error handling. So what codes are in error handling?")
        print("\t TRY (for testing block of codes for error) \n\t EXCEPT (used for blocking different errors)")
        print("\t FINALLY (runs whether there's an error or not) \n\t ELSE (runs if there's no error in try block)")
        num = int(input("\n\t Enter a number: "))
        try:
            print(10/num)
        except ValueError:
            print("\n\t (Value error) Please enter a valid number. ")
        except ZeroDivisionError:
            print("\n\t (Zero division error) You can't divide by zero.")
        else:
            print(f"\n\t (else:) You entered: {num}")

    elif que == "4d":
        print("\n\t Python, a high-level programming language, was designed by Guido van Rossum in 1991")
        print("\t and developed by the Python Software Foundation. Its syntax enables code readability")
        print("\t and allows for fewer lines of code, inspired by the BBC TV show Monty Python's Flying Circus.")

    elif que == "5e":
        print("\n\t Variables: containers for storing data values created and assigned by the user and it's case-sensitive")
        print("\n\t String variables can be declared either by using single or double quotes. \n\t Example: print('word')")
        print("\n\t To get the data type of a variable use the type() function.")
        print("\n\t Example: x = 5, y = 'John' \n\t print(type(x)) \n\t print(type(y)) ")
        print("\n\t To specify the data type of a variable do casting. \n\t Example:")
        print("\t x = str(3) \t# x will be '3' \n\t y = int(3) \t# y will be 3 \n\t z = float(3) \t# z will be 3.0")

    elif que == "6f":
        print("\n\t Operators are used to perform operations.")
        print("\n\tArithmetic operators:  + ,  - ,  * ,  / ,  //  (floor division),  %  (modulo),  **  (exponentiation). ")
        print("\t Comparison operators:  ==  (equal to),  !=  (not equal to),  > ,  < ,  >= ,  <= . ")
        print("\t Logical operators: and (output is true if both are true), or (output is true if any are True), not (reverse result). ")
        print("\t Assignment operators:  = ,  += ,  -= ,  *= , etc. ")
        print("\t Membership operators:  in ,  not in . ")
        print("\t Identity operators:  is ,  is not .")

    elif que == "7g":
        print("\n\t Data types is used to understand how Python handles different kinds of information")
        print("\n\t Integers (int): Whole numbers (e.g., 10, -5, 0). ")
        print("\t Floating-point numbers ( float ): Numbers with decimal points (e.g., 3.14, -2.5). ")
        print("\t Strings (str): Sequences of characters (e.g., 'Hello', 'Python'). ")
        print("\t Booleans (bool): Represent truth values (True  or  False). ")
        print("\t Lists (list): Ordered, changeable sequences of items (e.g., [1, 2, 'a']).")
        print("\t Tuples (tuple): Ordered, immutable (unchangeable) sequences of items (e.g., (1, 2, 'a')). ")
        print("\t Sets (set): Unordered collections of unique items (e.g., {1, 2, 3}). ")
        print("\t Dictionaries (dict): Collections of key-value pairs (e.g., {'name' : 'Alice', 'age': 30}).")

    elif que == "8h":
        print("\n\t Control Flow:  This dictates the order in which code is executed.")
        print("\t Conditional statements ( if ,  elif ,  else ): Execute code blocks based on conditions.")
        print("\t Loops ( for ,  while ): Repeat code blocks multiple times.")
        print("\t For loops iterate over sequences.")
        print("\t While loops continue as long as a condition is true.")

    elif que == "9i":
        print("\n\t  Input/Output:")
        print("\t print() : Displays output to the console.")
        print("\t input() :  Gets input from the user.")
        print("\t You can use #comment to serve as your guide/info in your code as well as docstrings")

    else:
        print("\n\t Please choose from the given additional topics ^w^")
def print_state():
    print("\t === This is about PRINT STATEMENTS ===")
    print("\n\t Just type: print('word') to display the output on screen")
    print("\t Example: print('Hello, world!')")
    print("\t name = 'Alice' \n\t print(f'My name is {name}') \t # f-string formatting ")
    print("\t print('The value of x is:'', 10)")

def esc():
    print("\t === This is about ESCAPE SEQUENCE ===")
    print("\\n - means next line  \t \\t - means space tab  \t \\b - for back space  \t \\r - for carriage return")
    print("\n\t Used in \n\t\t\t\t === ALL Activities ===")

def arith():
    print("\t === This is about ARITHMETIC SEQUENCE ===")
    print("\n\t Arithmetic sequence is a sequence of numbers in which specific operators are used. ")

def assign():
    print("\t === This is about ASSIGNMENT OPERATORS ===")
    print("\n\t Assignment operators, such as =, used to assign values to variables")
    print("\t and perform additional operations during the assignment process.")

def rel():
    print("\t === This is about RELATIONAL OPERATORS ===")
    print("\n\t Relational operators compare numeric, character string, or logical data to know ")
    print("\t if they're true (1) or false (0) to aid program flow.")
    print("\n\t Used in \n\t\t\t\t === Activities with If-Else Statements ===")

def logic():
    print("\t === This is about LOGICAL OPERATORS ===")
    print("\n\t Logical operators are crucial in conditional statements like if-else statements")
    print("\t It helps in in decision-making to determine the next action based on set conditions.")

def con():
    print("\t === This is about CONDITIONAL STATEMENTS ===")
    print("\n\t Python's conditional statements execute code based on a condition's truth value")
    print("\t with common types including if, elif, and else. ")
    print("\t Other types include if-else, elif, nested if, and nested if-else, controlling program execution.")

def f_loop():
    print("\t === This is about FOR LOOP ===")
    print("\n\t For loop is used to iterate over a sequence (list, tuple, or string) or other iterable objects.")

def wh():
    print("\t === This is about WHILE LOOP ===")
    print("\n\t A while loop executes a statement if a predetermined condition is true or have continue command.")
    print("\t It checks if it remains true after each iteration, and end if it is false or have a break command.")

def exit():
    print(f"\n\t Thank you for viewing this program {name}. Have a pleasant day and good luck! \(^w^)")
start = True
while start:   #Main options
    question()
    print("="*130,"\n\t A - Activities   \t   B - Code Challenges   \t   C - Surprise   \t   D - Additional Info   \t   E - Exit \n\t ")  
    main = input("Your decision: ")
    if main.lower() == "a": #Sub menu
        tops()
        sub = input("\n\t Choose a topic to view for each Activites: ")
        if sub == "1": 
            print_state()
            print("\n\t\t\t\t === Activity 1 ===")
            print("Hello World") 

            print("\n\t\t\t\t === Activity 3 ===")
            full_name = input("\n\n\t\t\t\t\t Bio-Data \n\n\t Please type your Name: ")
            gender = input("\t Please type your Gender: ")
            age = input("\t Please type your Age: ")
            BDate = input("\t Please type your Date of Birth: ")
            Brgy = input("\t Please type your Barangay name: ")
            ProvAd = input("\t Please type your Provincial Name: ")
            print("\n\t\t\t\t FAMILY DETAILS")
            Fn = input("\t Father's name: ")
            Mn = input("\t Mother's name: ")
            print("\n\t\t\t\t CONTACT DETAILS ")
            ConDe = input("\t Contact No.: ")
            ConD = input("\t E-mail Address: ")
            print("\n\n\t\t\t Hi, I am" , full_name, gender , "and I am" , age , "years old. I was born on" , 
            BDate , " I live in", Brgy, ProvAd, ". \n My father is" , Fn , "and my mother is" , Mn, 
            ".  You can contact me with my cellphone number," , ConDe , "and an e-mail of \n\t" , ConD,"." )
            continue

        elif sub == "2":  
            esc()
            continue

        elif sub == "3": 
            arith()
            print("\n\t\t\t\t === Activity 2 ===")
            num1 = eval(input("\n Please input a number: "))
            num2 = eval(input("\n Please input another number: "))
            print(num1, "Floor divided to", num2, "=", num1 // num2 )

            print("\n\t\t\t\t === Activity 4 ===")
            n1 = eval(input("\n\t Enter the first number: "))
            n2 = eval(input("\t Enter the second number: "))
            print("\n\t", n1, "+", n2, "is", n1 + n2, "\b. \n\t", n1, "-", n2, "is", n1 - n2, "\b.")
            print("\t", n1, "*", n2, "is", n1 * n2, "\b. \n\t", n1, "/", n2, "is", n1 / n2, "\b.")
            print("\t", n1, "exponent by", n2, "is", n1 ** n2, "\b.\n\t", n1, "%", n2, "is", n1 % n2, "\b.")
            print("\t", n1, "//", n2, "is", n1 // n2, "\b.")

            print("\n\t\t\t\t === Activity 5 ===")
            print("\n\t =====================================================")
            fahrenheit = eval(input("\n\t Enter temperature in Fahrenheit: "))
            celsius = ((fahrenheit - 32) * 5) /9
            print(f"\t {fahrenheit} degrees Fahrenheit converted to celsius is {round(celsius, 2)} degrees")                   
            continue

        elif sub == "4": 
            assign()
            print("\n\t\t\t\t === Activity 6 ===")
            x = 5
            x += 10
            print(x)
            continue
            
        elif sub == "5": 
            rel()
            continue

        elif sub == "6": 
            logic()
            print("\n\t\t\t\t === Activity 9 ===")
            age = eval(input("\n\t Enter your age: "))       #age category
            if age >=1 and age <=7:
                print("\n\t That age is categorized as a TODDLER.")
            elif age >=8 and age <=13:
                print("\n\t You're a PRE TEEN.")
            elif age >=14 and age <=18:
                print("\n\t Ooohh you're a TEENAGER.")
            else:
                print("\n\t Grabe ^O^ true ba?")
            continue
                    
        elif sub == "7": 
            con()
            print("\n\t\t\t\t === Activity 7 ===")
            gold = 1      #introduction to conditional statements
            miner = input("\n\t Hi, what's your name: ")
            isGold = input("\t Is the mineral gold? ")
            if isGold == "yes":
                gold += 5
                print(f"\n\t Hello {miner}, your total number of gold is {gold}")
            else:
                print(f"\n\t Hello {miner}, your total number of gold is {gold}")

            print("\n\t\t\t\t === Activity 8 ===")
            password = input("\n\t Enter your password: ")
            if password.lower() == "secret":
                print("\n\t Access Granted \n\t Enjoy using the system :> ")
            elif password.lower() == "letitgo123":
                print("\n\t Ay shala si Elsa pala itu. \n\t Access Granted")
            else:
                print("\n\t Access Denied")
            print("\n\t System Exit")

            print("\n\t\t\t\t === Activity 9 ===")
            age = eval(input("\n\t Enter your age: "))       #age category
            if age >=14 and age <=18:
                print("\n\t Ooohh you're a TEENAGER.")
            elif age >=19 and age <=31:
                print("\n\t That age is in EARLY ADULTHOOD.")
            elif age >=32 and age <=45:
                print("\n\t That age is in MID ADULTHOOD.")
            elif age >=46 and age <=59:
                print("\n\t That age is in POST ADULTHOOD.")
            elif age >=60 and age <=120:
                print("\n\t You're considered as a SENIOR.")
            else:
                print("\n\t Grabe ^O^ true ba?")
                
            print("\n\t\t\t\t === Activity 10 ===")
            namee = input("\n\t Enter your name: ")     #Python Demo for NESTED CONDITION  #Data Filtration Program
            isStudent = input("\n\t Are you a current student of DLL (yes/no): ")
            if isStudent.lower() == "yes":
                print("\n\t What year are you currently enrolled? \n\t F - Freshmen \n\t S - Sophomore \n\t J - Junior \n\t R - Senior ")
                yearLevel = input("\n\t Please enter your answer here:  ")
                if yearLevel.lower() == "f":
                    print(f"\n\t Hi {namee}, our dear freshmen. Welcome to DLL ^w^")
                elif yearLevel.lower() == "s":
                    print(f"\n\t Hi {namee}, our dear sophomore. Welcome to DLL ^w^")
                elif yearLevel.lower() == "j":
                    print(f"\n\t Hi {namee}, one of our junior. Welcome to DLL ^w^")
                elif yearLevel.lower() == "r":
                    print(f"\n\t Hi {namee}, one of our senior. Welcome to DLL ^w^")
                else:
                    print("\n\t You've entered a different answer. Try again.")
            else:
                print("Thank you for using the system.")
            continue
        
        elif sub == "8": 
            f_loop()
            print("\n\t\t\t\t === Activity 11 ===")
            for q in range(1,11):        #print a word 10 times
                print(q, "Hello World \n\t\t Happy, shalalala~ ")

            print("\n\t\t\t\t === Activity 12 ===")
            for s in range(10, 0, -1):        # understand range parameters
                print(s)

            print("\n\t\t\t\t === Activity 13 ===")
            numm = eval(input("\n\t Enter a number: "))       #make factorial of given number
            fac = 1
            for x in range(1, numm+1):
                fac = fac * x
            print(f"\n\t The factorial of {numm} is {fac}.")

            print("\n\t\t\t\t === Activity 14 ===")
            for t in range(0,11):        #washing machine
                # print("*", end = "-") #laundry  #another washing machine
                print(t, end = " ")
                for u in range(0,11):
                    print("*",end=" ")
                print()

            print("\n\t\t\t\t === Activity 15 ===")
            for v in range(0,11):        #triangle with numbers
                print(v, end = " ")
                for w in range(0, v):
                    print("*", end = " ")
                print()

            print("\n\t\t\t\t === Activity 16 ===")
            for a in range(-1,5):       #make an inverted triangle
                for b in range(-1, a+1):
                    print(" ", end=" ")
                for c in range(5, a, -1):
                    print("*", end=" ")
                for d in range(4, a, -1):
                    print("*", end=" ")
                print()

            print("\n\t\t\t\t === Activity 17 ===")
             #create a multiplication table depends on the number given by the user
            col = eval(input("\n Enter a number of columns: "))
            for x in range(1,11):
                for y in range(1, col +1):
                    print(x*y, end= "\t")
                print()

            print("\n\t\t\t\t === Activity 18 ===")
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
            
        elif sub == "9": 
            wh()
            print("\n\t\t\t\t === Activity 19 ===")
            go = True          #Print hi, name until the user types 'stop'
            while go:
                nm = input("\n\t Type any name ('stop' to end): ")
                if nm.lower() == "stop":
                    print("\n\t LOOP TERMINATED \n", "="*120)
                    break
                    go = False
                else:
                    print(f"\n\t Hi {nm} ^w^.")
                    continue

            print("\n\t\t\t\t === Activity 20 ===")
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

            print("\n\t\t\t\t === Activity 21 ===")
            #keep on asking for a name until user types stop, once the loop stopped count the number of names given
            count = 0
            while True:
                name = input("\n\t Please enter a name (type 'stop' to end): ") 
                if name.lower() == "stop":
                    print("\n\t Loop has now stopped") 
                    print(f"\n\t You have entered {count} number of names. ") 
                    break
                else:
                    count += 1 
                    continue
            continue
                    
        elif sub == "10": 
            print("\t === This is about FUNCTION ===")
            print("\n\t Function is a block of code that only runs when it's called")

            print("\n\t\t\t\t === Activity 22 ===")
            print(" Example: def panghello(): \n\t Hello dear IT1A")
            continue
            
        elif sub == "11": 
            print("\t === This is about FUNCTION w/ RETURN STATEMENT ===")
            print("\n\t\t\t\t === Activity 23 ===")
            print(" fact = 1 \n\t for x in range(num, 0, -1): \n\t\t fact *= x \n\t return fact")
            continue

        elif sub == "12": # DOCUMENTATION STRING
            print("\t === This is about DOCUMENTATION STRING ===")
            print("\n\t Docstring is a string used to document a Python module, class, function or method. ")
            print("\n\t\t\t\t === Activity 23 ===")
            print("\t from activity23 import factorial \n f'n\t The factorial of 5 is {factorial(5)}' and type")
            print("\t help(factorial) to display docstrings with instruction/note")
            continue

        elif sub == "13": # MODULE
            print("\n\t Module are files that contain python codes that uses the word 'import' ")
            print("\n\t Example:   from activity24 import factorial")
            print("\n\t\t\t\t === Activity 24 ===")
            print("\n\t from activity24 import factorial \n\t as well as import os.")
            continue

        elif sub == "14": # LIST
            print("\n\t List is an ordered, changeable sequences of items. You can add, insert and remove an item.")
            print("\n\t Example: my_list = [1, 2, 3, 'a', 'b']")
            print("\n\t To access the first element, type print(my_list[0])")
            print("\n\t To add an element, type my_list.append(4)")  
            print("\n\t To insert an element to a desired place, type my_list.insert(2)")
            print("\n\t To remove an element, type my_list.remove('a')")
            print("\n\t You can use my_list.pop() to pop an element from a list")
            print("\n\t To add elements of an iterable to end of other list, type my_list.extend()")

            print("\n\t\t\t\t === Activity 25 ===")
            # fruit1 = "apple"
            # fruit2 = "persimmon"   #index  - the location of the item inside that starts with 0
            fruits = ["apple", "mango", "orange", "melon"]
            print(fruits)
            #access item individually
            print(f"My favorite fruit growing up is {fruits[0]}.")
            #add more item
            fruits.append("strawberry")
            print(fruits)
            fruits.insert(3, "watermelon")
            print(fruits)
            continue
            
        else:
            close = input("Are you trying to exit? ")
            if close.lower() =="yes":
                exit()
            else:
                continue

        
    elif main.lower() == "b": #Sub menu
        tops2()
        sub2 = input("\n\t Choose a topic to view for Code Challenges: ")     
        if sub2 == "1a": 
            print_state()
            print("\n\t\t\t\t === Code Challenge 3 ===")
            full_name = input("\n\n\t\t\t\t\t Bio-Data \n\n\t Please type your Name: ")
            gender = input("\t Please type your Gender: ")
            age = input("\t Please type your Age: ")
            BDate = input("\t Please type your Date of Birth: ")
            Brgy = input("\t Please type your Barangay name: ")
            ProvAd = input("\t Please type your Provincial Name: ")
            print("\n\t\t\t\t FAMILY DETAILS")
            Fn = input("\t Father's name: ")
            Mn = input("\t Mother's name: ")
            print("\n\t\t\t\t CONTACT DETAILS ")
            ConDe = input("\t Contact No.: ")
            ConD = input("\t E-mail Address: ")
            print("\n\n\t\t\t Hi, I am" , full_name, gender , "and I am" , age , "years old. I was born on" , 
                BDate , " I live in", Brgy, ProvAd, ". \n My father is" , Fn , "and my mother is" , Mn, 
                ".  You can contact me with my cellphone number," , ConDe , "and an e-mail of \n\t" , ConD,"." )
                    
        elif sub2 == "2a": 
            esc()
            print("\n\t\t\t\t === Code Challenge 1 ===")
            from challenge_files import cc1
            cc1()
            print("\n\t\t\t\t === Code Challenge 2 ===")
            from challenge_files import cc2
            cc2()

        elif sub2 == "3a":
            arith() 
            print("\n\t\t\t\t === Code Challenge 4 ===")
            from challenge_files import cc4
            cc4()
            print("\n\t\t\t\t === Code Challenge 5 ===")
            from challenge_files import cc5
            cc5()

            pass
        elif sub2 == "4a": 
            assign()
            print("\n\t\t\t\t === Code Challenge 7 ===")
            from challenge_files import cc7
            cc7()

            pass
        elif sub2 == "5a": 
            rel()
            print("\n\t\t\t\t === Code Challenge 6 ===")
            from challenge_files import cc6
            cc6()

        elif sub2 == "6a": 
            logic()
            print("\n\t\t\t\t === Code Challenge 6 ===")
            from challenge_files import cc6
            cc6()

            
        elif sub2 == "7a": 
            con()
            print("\n\t\t\t\t === Code Challenge 6 ===")
            from challenge_files import cc6
            cc6()
            print("\n\t\t\t\t === Code Challenge 7 ===")
            from challenge_files import cc7
            cc7()

        elif sub2 == "8a": 
            f_loop()
            print("\n\t\t\t\t === Code Challenge 8 ===")
            time.sleep(1)
            from challenge_files import cc8
            cc8()
            print("\n\t\t\t\t === Code Challenge 9 ===")
            from challenge_files import cc9
            cc9()
            time.sleep(2)
            print("\n\t\t\t\t === Code Challenge 10 ===")
            from challenge_files import cc10
            cc10()
            time.sleep(3)
            print("\n\t\t\t\t === Code Challenge 11 ===")
            from challenge_files import cc11
            cc11()
            time.sleep(2)
            print("\n\t\t\t\t === Code Challenge 12 ===")
            from challenge_files import cc12
            cc12()
            time.sleep(2)
            print("\n\t\t\t\t === Code Challenge 13 ===")
            from challenge_files import cc13
            cc13()
            continue
            
        elif sub2 == "9a": 
            wh()
            print("\n\t\t\t\t === Code Challenge 14 ===")
            from challenge_files import cc14
            cc14()
            print("\n\t\t\t\t === Code Challenge 15 ===")
            from challenge_files import cc15
            cc15()
            print("\n\t\t\t\t === Code Challenge 16 ===")
            from challenge_files import cc16
            cc16()
            
        else:
            close = input("Are you trying to exit? ")
            if close.lower() =="yes":
                exit()
            else:
                continue

    elif main.lower() == "c": #Additional output
        from Surprise import surprise
        surprise()
        continue

    elif main.lower() == "d":
        add()
        continue

    elif main.lower() == "e":
        exit()
        break

    else:
        print("\n\t Please choose from the given.")
        continue