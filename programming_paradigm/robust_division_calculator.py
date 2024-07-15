def safe_divide(numerator, denominator):
    return numerator/denominator

numerator = input(float("numerator"))
denominator = input(float("denominator"))

try:
    safe_divide()
except ZeroDivisionError :
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter numeric values only.")



