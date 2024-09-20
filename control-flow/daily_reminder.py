
task = input("Enter your task: ").strip()

while True:
    priority = input("Priority (high/medium/low): ").strip().lower()
    if priority in ['high', 'medium', 'low']:
        break
    else:
        print("Invalid priority level. Please enter 'high', 'medium', or 'low'.")

while True:
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    if time_bound in ['yes', 'no']:
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

match priority:
    case 'high':
        reminder = f"'{task}' is a high priority task"
    case 'medium':
        reminder = f"'{task}' is a medium priority task"
    case 'low':
        reminder = f"'{task}' is a low priority task"

if time_bound == 'yes':
    reminder += ". that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

print(f"\nReminder: {reminder}")
