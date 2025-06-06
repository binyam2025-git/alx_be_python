CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_OFFSET = 32

def convert_celsius_to_fahrenheit(celsius_temp):
    """
    Converts a temperature from Celsius to Fahrenheit.
    """
    return (celsius_temp * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET

def convert_fahrenheit_to_celsius(fahrenheit_temp):
    """
    Converts a temperature from Fahrenheit to Celsius.
    """
    return (fahrenheit_temp - FAHRENHEIT_OFFSET) / CELSIUS_TO_FAHRENHEIT_FACTOR

def main():
    """
    Main function for user interaction and temperature conversion.
    """
    while True:
        print("\nTemperature Conversion Tool")
        print("1. Convert Celsius to Fahrenheit")
        print("2. Convert Fahrenheit to Celsius")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ").strip()

        if choice == '1':
            while True:
                try:
                    celsius_str = input("Enter temperature in Celsius: ").strip()
                    celsius = float(celsius_str)
                    fahrenheit = convert_celsius_to_fahrenheit(celsius)
                    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
                    break
                except ValueError:
                    print("Invalid input. Please enter a numerical value for temperature.")
        elif choice == '2':
            while True:
                try:
                    fahrenheit_str = input("Enter temperature in Fahrenheit: ").strip()
                    fahrenheit = float(fahrenheit_str)
                    celsius = convert_fahrenheit_to_celsius(fahrenheit)
                    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
                    break
                except ValueError:
                    print("Invalid input. Please enter a numerical value for temperature.")
        elif choice == '3':
            print("Exiting temperature conversion tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
