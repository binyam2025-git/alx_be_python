print("--- Task Reminder setup ---")

task_description = input("Enter your task:")
priority_input = input("Priority (high/medium/low):").lower()
is_time_bound = input("Is it time-bound? (yes/no):").lower() == 'yes'

reminder_message = ""

match priority_input:
    case "high":
        reminder_message = f"Reminder: '{task_description}' is a high priority task"
    case "medium":
        reminder_message = f"Reminder: '{task_description}' is a medium priority task"
    case "low":
        reminder_message = f"Reminder: '{task_description}' is a low priority task"
    case _:
        reminder_message = f"Reminder: '{task_description}' has an unspecified priority"

if is_time_bound:
    reminder_message += " that requires immediate attention today!"
else:
    reminder_message += ". Consider completing it when you have free time."

print("\n--- Your Customized Reminder ---")
print(reminder_message)
