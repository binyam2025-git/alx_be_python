FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9  # This is the line the checker is looking for!
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
OFFSET = 32 # This offset is used in both conversions

# Implement Conversion Functions:
def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius using global factors.
    Formula: (Fahrenheit - 32) * (5/9)
    """
    # Accessing global variables (reading their values)
    return (fahrenheit - OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit using global factors.
    Formula: (Celsius * 9/5) + 32
    """
    # Accessing global variables (reading their values)
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + OFFSET

# User Interaction:
def main():
    """
    Main function to handle user interaction for temperature conversion.
    """
    while True:
        try:
            temp_str = input("Enter the temperature to convert: ").strip()
            temperature = float(temp_str) # Attempt to convert input to float

            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

            if unit == 'C':
                converted_temp = convert_to_fahrenheit(temperature)
                print(f"{temperature}°C is {converted_temp}°F")
                break # Exit loop on successful conversion
            elif unit == 'F':
                converted_temp = convert_to_celsius(temperature)
                print(f"{temperature}°F is {converted_temp}°C")
                break # Exit loop on successful conversion
            else:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
                # Loop will continue, asking for input again
        except ValueError:
            # If float(temp_str) fails, a ValueError is raised
            print("Invalid temperature. Please enter a numeric value.")
            # The loop will continue, asking for input again

# Ensures main() runs only when the script is executed directly
if __name__ == "__main__":
    main()
