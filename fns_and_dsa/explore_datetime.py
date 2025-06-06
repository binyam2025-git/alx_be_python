from datetime import datetime, timedelta

def display_current_datetime():
    """
    Obtains the current date and time, saves it, and prints it in
    "YYYY-MM-DD HH:MM:SS" format.
    """
    # Research: datetime.now() gets the current local date and time
    current_date = datetime.now()
    
    # Format and print the current date and time
    # Research: strftime() is used for formatting datetime objects
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")
    
    # Return current_date for potential use in other functions, though not strictly required by task
    return current_date

def calculate_future_date():
    """
    Prompts the user for a number of days, calculates a future date
    from the current date, and prints it in "YYYY-MM-DD" format.
    """
    # Get the current date and time for the calculation's base
    current_moment = datetime.now() 

    while True:
        try:
            days_str = input("Enter the number of days to add to the current date: ").strip()
            num_of_days = int(days_str)
            break # Exit loop if input is a valid integer
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Research: timedelta is used to represent a duration (like a number of days)
    # Add the timedelta to the current date to get the future date
    future_date = current_moment + timedelta(days=num_of_days)
    
    # Format and print the future date
    # Research: strftime() is used for formatting datetime objects, again
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

def main():
    """
    Main function to orchestrate the datetime exploration tasks.
    """
    display_current_datetime()
    print("-" * 30) # Separator for readability
    calculate_future_date()

# Ensures main() runs only when the script is executed directly
if __name__ == "__main__":
    main()
