FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.
    Uses the global FAHRENHEIT_TO_CELSIUS_FACTOR.
    Formula: C = (F - 32) * (5/9)
    """
    # Accessing the global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.
    Uses the global CELSIUS_TO_FAHRENHEIT_FACTOR.
    Formula: F = C * (9/5) + 32
    """
    # Accessing the global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

def main():
    """
    Main function to interact with the user, get input, perform conversion,
    and display the result. Handles input validation.
    """
    print("--- Temperature Conversion Tool ---")

    # Prompt user for temperature
    temperature_input = input("Enter the temperature to convert: ").strip()
    
    # Input validation for numeric value
    try:
        temperature = float(temperature_input) # Use float for temperatures
    except ValueError:
        # If the input is not a valid number, print the error message and exit
        print("Invalid temperature. Please enter a numeric value.")
        return # Exit the function, ending the script for this run

    # Prompt user for unit
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
    elif unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

# Ensures main() runs only when the script is executed directly
if __name__ == "__main__":
    main()
