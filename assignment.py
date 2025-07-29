num1 = float (input("enter the first number: "))
num2 = float (input("input the second number: "))
operator = input("enter operator (+,-,*,/): ")

# perform the calclationbased on the operator
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2 
elif operator == '/':
    if num2 !=0:
      result = num1 / num2
    else:
         result = "error: division by zero is not allowed."
else:
    result = "error: division by zero is not allowed."
print(f"the result is: {result}")
    