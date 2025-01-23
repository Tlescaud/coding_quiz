def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return celsius_to_fahrenheit(value)
        elif to_unit == 'Kelvin':
            return celsius_to_kelvin(value)
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return fahrenheit_to_celsius(value)
        elif to_unit == 'Kelvin':
            return fahrenheit_to_kelvin(value)
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return kelvin_to_celsius(value)
        elif to_unit == 'Fahrenheit':
            return kelvin_to_fahrenheit(value)
    else:
        return "Invalid input"

def main():
    value = float(input("Enter the temperature value: "))
    from_unit = input("Enter the source unit (Celsius, Fahrenheit, Kelvin): ").capitalize()
    to_unit = input("Enter the target unit (Celsius, Fahrenheit, Kelvin): ").capitalize()
    result = convert_temperature(value, from_unit, to_unit)
    print(f"{value} {from_unit} is equal to {result} {to_unit}")

# Example usage
main()


'''

In this program:

We have defined several functions to handle the conversions between Celsius, Fahrenheit, and Kelvin.

The convert_temperature function determines the conversion to perform based on the source and target units.

The main function gets the temperature value and units from the user, performs the conversion, and prints the result.

Feel free to run this program and try converting different temperatures! If you have any questions or need further assistance, just let me know.

'''