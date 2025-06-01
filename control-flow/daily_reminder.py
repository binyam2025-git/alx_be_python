print("--- Task Reminder setup ---")

task = input("Enter your task:")
priority = input("Priority (high/medium/low):").lower()
time_bound = input("Is it time-bound? (yes/no):").lower()

match priority:
    case "high":
        reminder_text = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder_text = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder_text = f"Reminder: '{task}' is a low priority task"
    case _:
        reminder_text = f"Reminder: '{task}' has an unspecified priority"

print("\n--- Your Customized Reminder ---")
if time_bound == "yes":
    print(f"{reminder_text} that requires immediate attention today!")
else:
    print(f"{reminder_text}. Consider completing it when you have free time.")



