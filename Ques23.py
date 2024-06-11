def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").upper()

if unit == 'C':
    converted_temp = celsius_to_fahrenheit(temperature)
    print(f"{temperature}°C is equivalent to {converted_temp}°F.")
elif unit == 'F':
    converted_temp = fahrenheit_to_celsius(temperature)
    print(f"{temperature}°F is equivalent to {converted_temp}°C.")
else:
    print("Invalid unit. Please enter either C or F.")
