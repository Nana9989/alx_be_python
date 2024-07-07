FARENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FARENHEIT_FACTOR = 9/5

def convert_to_celsius(farenheit):
    answer = (farenheit - 32)*FARENHEIT_TO_CELSIUS_FACTOR
    return answer

def convert_to_farenheit(celsius):
    answer = (celsius * CELSIUS_TO_FARENHEIT_FACTOR) + 32
    return answer

temperature = int(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Farenheit? (C/F): ")



