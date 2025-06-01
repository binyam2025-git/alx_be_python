print("--- Task Reminder setup ---")

task = input("Enter your task:")
priority = input("Priority (high/medium/low):").lower()
time_bound = input("Is it time-bound? (yes/no):").lower()

match priority:
    case "high":
        base_msg = f"Reminder: '{task}' is a high priority task"
    case "medium":
        base_msg = f"Reminder: '{task}' is a medium priority task"
    case "low":
        base_msg = f"Reminder: '{task}' is a low priority task"
    case _:
        base_msg = f"Reminder: '{task}' has an unspecified priority"

if time_bound == "yes":
    print("\n--- Your Customized Reminder ---")
    print(f"{base_msg} that requires immediate attention today!")
else:
    print("\n--- Your Customized Reminder ---")
    print(f"{base_msg}. Consider completing it when you have free time.")



