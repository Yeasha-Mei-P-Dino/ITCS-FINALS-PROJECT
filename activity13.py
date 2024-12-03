#make factorial of given number

num = eval(input("\n\t Enter a number: "))
fac = 1
for x in range(1, num+1):
    fac = fac * x
print(f"\n\t The factorial of {num} is {fac}.")