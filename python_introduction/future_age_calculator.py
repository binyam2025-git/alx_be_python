# Prompt the user for their current age
# input() reads a string, so we convert it to an integer using int()
current_age_str = input("How old are you? ")
current_age = int(current_age_str)

# Define the number of years to add to reach 2050 (2050 - 2023 = 27)
years_to_add = 27

# Calculate the age in 2050
future_age = current_age + years_to_add

# Print the result in the specified format
print(f"In 2050, you will be {future_age} years old.")
