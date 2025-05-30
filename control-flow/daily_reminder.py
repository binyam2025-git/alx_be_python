def create_daily_reminder():
    """
    Prompts the user for a single task, its priority, and time sensitivity,
    then provides a customized reminder.
    """
    # Prompt for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    reminder_message = f"Note: '{task}' is a {priority} priority task."

    # Process the task based on priority and time sensitivity using match case
    match priority:
        case 'high':
            # High priority tasks often need strong wording
            reminder_message = f"Reminder: '{task}' is a HIGH priority task."
            if time_bound == 'yes':
                reminder_message += " that requires immediate attention today!"
            else:
                reminder_message += ". Aim to complete it as soon as possible."
        case 'medium':
            reminder_message = f"Reminder: '{task}' is a medium priority task."
            if time_bound == 'yes':
                reminder_message += " that requires immediate attention today!"
            else:
                reminder_message += ". Plan to tackle it soon."
        case 'low':
            reminder_message = f"Note: '{task}' is a low priority task."
            if time_bound == 'yes':
                reminder_message += " that requires immediate attention today!"
            else:
                reminder_message += ". Consider completing it when you have free time."
        case _: # Handles invalid priority input
            print("Invalid priority level entered. Please choose high, medium, or low.")
            return # Exit the function if priority is invalid

    print(reminder_message)

# Call the function to run the daily reminder program
if __name__ == "__main__":
    create_daily_reminder()
