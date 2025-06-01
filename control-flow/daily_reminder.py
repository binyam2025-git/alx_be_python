print("--- Task Reminder Setup ---")

task_description = input("Enter your task description: ")

# Validate priority input using a loop
valid_priorities = {'high', 'medium', 'low'}
while True:
    priority_input = input("Priority (high/medium/low): ").lower()
    if priority_input in valid_priorities:
        break
    print("Invalid input. Please enter 'high', 'medium', or 'low'.")

is_time_bound = input("Is the task time-bound? (yes/no): ").lower() == 'yes'

reminder_message = ""
match priority_input:
    case 'high':
        reminder_message = f"Reminder: '{task_description}' is a high priority task"
    case 'medium':
        reminder_message = f"Reminder: '{task_description}' is a medium priority task"
    case 'low':
        reminder_message = f"Reminder: '{task_description}' is a low priority task"

if is_time_bound:
    reminder_message += " that requires immediate attention today!"
else:
    reminder_message += ". Consider completing it when you have free time."

print("\n--- Your Customized Reminder ---")
print(reminder_message)
