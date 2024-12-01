
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