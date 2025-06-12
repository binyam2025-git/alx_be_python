def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)

        if den == 0:
            # This message already matches the expected output
            return "Error: Cannot divide by zero."
        result = num / den
        # This message already matches the expected output format
        return f"The result of the division is {result}"

    except ValueError:
        # CORRECTED LINE: Changed 'please' to 'Please'
        return "Error: Please enter numeric values only."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
