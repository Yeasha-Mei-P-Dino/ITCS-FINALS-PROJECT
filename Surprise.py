import os
import time #Christmas tree and greetings for viewer 

def tri(n):
    for i in range(n):
        for j in range(n-1):
            print(' ',end=" ")
        for k in range(i+1):
            print("*", end=" ")
        print()
def base(n):
    for i in range(n):
        for j in range(n-1):
            print(" ", end=" ")
        print("***")
    for m in range(5):
        print("**", end="")

def greet():
    print("\n\t Merry Christmas and Happy New Year to you! ^w^")
    rows = int(input("\n\t Enter number of rows: "))
    # height = int(input("\n\t Enter a height: "))
    tri(rows)
    tri(rows)
    base(rows)

    

    
def surprise():
    os.system('cls')
    time.sleep(1)
    name = input("\n\t Enter your name please: ")
    ask = input("\t Are you a catholic? ")
    if ask.lower() == "yes":

        song = input("\n\t Enter a number from 1-5 please: ")
        if song.lower() == "1":
            greet()
            time.sleep(1)
            print("\n Ang liwanag na ito \n Nasa 'ting lahat \n May sinag ang bawat pusong bukas")
            print("Sa init ng mga yakap \n Maghihilom ang lahat ng sugat \n Ang nagsindi nitong ilaw")
            time.sleep(1)
            print("Walang iba kundi ikaw \n Salamat sa liwanag mo \n Muling magkakakulay ang pasko")
            print("Salamat sa liwanag mo \n Muling magkakakulay ang pasko ohohh")
            print("Kikislap ang pag-asa \n Kahit kanino man")
            print("Dahil ikaw bro dahil ikaw bro (dahil ikaw bro)")
            time.sleep(1)
            print("Dahil ikaw bro dahil ikaw bro (dahil ikaw bro)")
            print("Ikaw ang star ng pasko (ikaw ang star ng pasko~)")
            print(f"\t Mamamasko po {name}! ^V^ ")
            ans = input("\n\t Food, grades or whatever pls^w^: ")
            if ans.lower() == "food":
                print("\t Yey, soon thankieee")
                print("\t Thank you, thank you. Ang babait ninyo thank you!")
            elif ans.lower() == "grades":
                print("\t Beke nemen po Sir HAHAHA")
            else:
                print("\n\t Luh oki, thanks pa rin T^T")

        elif song.lower() == "2":
            greet()
            print("\n Tuwing Pasko, whoa-oh-whoa \n Mas ramdam mo, whoa-oh-whoa \n Dama sa ating tinig ang init ng pag-ibig")
            print("Oh, whoa-oh \n Na-na-na-na-na-na-na-na \n Thank you, thank you for the love")
            print("Na-na-na-na-na-na-na-na \n Thank you, thank you for the love!")
            time.sleep(1)
            print(f"\t Mamamasko po {name}! ^V^ ")
            ans = input("\n\t Food, grades or whatever pls^w^: ")
            if ans.lower() == "food":
                print("\t Yey, soon thankieee")
                print("\t Thank you, thank you. Ang babait ninyo thank you!")
            elif ans.lower() == "grades":
                print("\t Beke nemen po Sir HAHAHA")
            else:
                print("\n\t Luh oki, thanks pa rin T^T")
                
        elif song.lower() == "3":
            greet()
            print("\n We wish you a Merry Christmas"*3)
            time.sleep(1)
            print("And a happy new year \n Good tidings we bring \n To you and your kin \n Good tidings for Christmas")
            time.sleep(1)
            print("And a happy new year", "\n We wish you a merry Christmas"*3, "\n And a happy new year")
            print(f"\t Mamamasko po {name}! ^V^ ")
            ans = input("\n\t Food, grades or whatever pls^w^: ")
            if ans.lower() == "food":
                print("\t Yey, soon thankieee")
                print("\t Thank you, thank you. Ang babait ninyo thank you!")
            elif ans.lower() == "grades":
                print("\t Beke nemen po Sir HAHAHA")
            else:
                print("\t Luh oki, thanks pa rin T^T")

        elif song.lower() == "4":
            greet()
            print("\n Pasko na naman o kay tulin ng araw")
            time.sleep(1)
            print("Paskong nagdaan tila ba kung kailan lang")
            print("Ngayon ay pasko dapat pasalamatan")
            print("Ngayon ay pasko tayo ay mag-awitan")
            print("Pasko pasko pasko na namang muli")
            print("Tanging araw na ating pinakamimithi")
            print("Pasko pasko pasko na namang muli")
            print("Ang pag-ibig naghahari")
            print(f"\t Mamamasko po {name}! ^V^ ")
            ans = input("\n\t Food, grades or whatever pls^w^: ")
            if ans.lower() == "food":
                print("\t Yey, soon thankieee")
                print("\t Thank you, thank you. Ang babait ninyo thank you!")
            elif ans.lower() == "grades":
                print("\t Beke nemen po Sir HAHAHA")
            else:
                print("\t Luh oki, thanks pa rin T^T")

        elif song.lower() == "5":
            greet()
            print("\n Feliz Navidad")
            time.sleep(1)
            print("Feliz Navidad")
            time.sleep(1)
            print("Feliz Navidad")
            print("Próspero año y felicidad")
            print("I wanna wish you a merry Christmas")
            print("I wanna wish you a merry Christmas")
            print("I wanna wish you a merry Christmas")
            time.sleep(1)
            print("From the bottom of my heart Navidad")
            time.sleep(1)
            print(f"\t Mamamasko po {name}! ^V^ ")
            ans = input("\n\t Food, grades or whatever pls^w^: ")
            if ans.lower() == "food":
                print("\t Yey, soon thankieee")
                print("\t Thank you, thank you. Ang babait ninyo thank you!")
            elif ans.lower() == "grades":
                print("\t Beke nemen po Sir HAHAHA")
            else:
                print("\t Luh oki, thanks pa rin T^T")
        else:
            print("\t Sana sinabi mo para di na umasang may pamasko sa huli~ ")
            print("-"*130)
    else:
        print(f"\n\t Happy holiday to you {name}! ^W^ Enjoy your vacation.")
        print("-"*130)

surprise()