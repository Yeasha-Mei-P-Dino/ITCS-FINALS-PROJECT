#Fetch 10 random numbers from the user and get the summation of it

sum = 0
for i in range(1,11):
    num = eval(input(f"\n\t  Enter a number {i}:"))
    sum += num

print(f"\n\t  The sum of all the numbers you entered is {sum}.")