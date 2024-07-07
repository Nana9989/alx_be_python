def perform_operation(num1, num2, operations):
 match operations:
     case "add":
         result = num1+num2
     case "subtract":
         result = num1-num2
     case "multiply":
         result = num1*num2
     case "divide":
         if num2 == 0:
             print("Invalid, cannot divide by zero")
         else:
             result = num1/num2
 return result


print("Arithmetic Operations")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

result = perform_operation(num1, num2, operation)
print(f"Result: {result}")