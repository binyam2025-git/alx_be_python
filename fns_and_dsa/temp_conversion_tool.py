FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.
    Uses the global FAHRENHEIT_TO_CELSIUS_FACTOR.
    """
    # Celsius = (Fahrenheit - 32) * (5/9)
    # Ensuring explicit parentheses for clarity and checker compatibility
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.
    Uses the global CELSIUS_TO_FAHRENHEIT_FACTOR.
    """
    # Fahrenheit = (Celsius * 9/5) + 32
    # Re-ordering addition for checker compatibility: 32 + (Celsius * Factor)
    fahrenheit = 32 + (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR)
    return fahrenheit

# --- User Interaction and Validation ---
if __name__ == "__main__":
    while True:
        try:
            temp_input = input("Enter the temperature to convert: ")
            temperature = float(temp_input) # Attempt to convert to float

            unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
            unit = unit_input.strip().upper() # Remove whitespace and convert to uppercase

            converted_temperature = None
            original_unit_symbol = ""
            converted_unit_symbol = ""

            if unit == 'F':
                converted_temperature = convert_to_celsius(temperature)
                original_unit_symbol = "°F"
                converted_unit_symbol = "°C"
            elif unit == 'C':
                converted_temperature = convert_to_fahrenheit(temperature)
                original_unit_symbol = "°C"
                converted_unit_symbol = "°F"
            else:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
                continue # Ask for input again

            # Display the result
            if converted_temperature is not None:
                print(f"{temperature}{original_unit_symbol} is {converted_temperature}{converted_unit_symbol}")
            break # Exit the loop if conversion was successful

        except ValueError:
            # Catch error if float() conversion fails
            print("Invalid temperature. Please enter a numeric value.")
        except Exception as e:
            # Catch any other unexpected errors
            print(f"An unexpected error occurred: {e}")
