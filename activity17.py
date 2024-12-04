#create a multiplication table depends on the number given by the user

col = eval(input("\n Enter a number of columns: "))

for x in range(1,11):
    for y in range(1, col +1):
        print(x*y, end= "\t")
    print()