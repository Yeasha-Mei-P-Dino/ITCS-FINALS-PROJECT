def factorial(num):
    """This function's purpose is to compute/calculate the factorial of any given number."""
    fact = 1
    for x in range(num, 0, -1):
        fact *= x
    return fact

print(f"\n\t The factorial of 5 is {factorial(5)}")
help(factorial)