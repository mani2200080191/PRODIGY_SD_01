def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature(value, unit):
    if unit.lower() == 'c':
        celsius = value
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
        print(f"{celsius}°C is equal to {fahrenheit}°F and {kelvin}K.")
    elif unit.lower() == 'f':
        fahrenheit = value
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius}°C and {kelvin}K.")
    elif unit.lower() == 'k':
        kelvin = value
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        print(f"{kelvin}K is equal to {celsius}°C and {fahrenheit}°F.")
    else:
        print("Invalid unit of measurement. Please use 'C' for Celsius, 'F' for Fahrenheit, or 'K' for Kelvin.")

def main():
    value = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of measurement (C/F/K): ")
    convert_temperature(value, unit)

if __name__ == "__main__":
    main()
