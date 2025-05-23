# User Input for Financial Details
# Convert input to float for potential decimal values in income/expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# Project Annual Savings
# Assume a simple annual interest rate of 5% (0.05)
annual_interest_rate = 0.05
projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)

# Output Results
print(f"Your monthly savings are ${monthly_savings:.2f}.") # .2f for 2 decimal places
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")
