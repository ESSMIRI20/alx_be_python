task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ")

time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case 'high':
        reminder = f"'{task}' is a high priority task"
        if time_bound == 'yes':
            reminder += " that requires immediate attention today!"
            print(f"Reminder: {reminder}")
        elif time_bound == 'no':
            reminder += ". Consider completing it when you have free time."
            print(f"Note: {reminder}")
        else:
            print("invalid input")
    case 'medium':
        reminder = f"'{task}' is a medium priority task"
        if time_bound == 'yes':
            reminder += " that requires immediate attention today!"
            print(f"Reminder: {reminder}")
        elif time_bound == 'no':
            reminder += ". Consider completing it when you have free time."
            print(f"Note: {reminder}")
        else:
            print("invalid input")
    case 'low':
        reminder = f"'{task}' is a low priority task"
        if time_bound == 'yes':
            reminder += " that requires immediate attention today!"
            print(f"Reminder: {reminder}")
        elif time_bound == 'no':
            reminder += ". Consider completing it when you have free time."
            print(f"Note: {reminder}")
        else:
            print("invalid input")
    case _:
        print("invalid input")
