while True:
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()

    if priority not in ["high", "medium", "low"]:
        print("Invalid priority entered. Defaulting to 'unspecified'.")
        priority = "unspecified"

   
    if time_bound not in ["yes", "no"]:
        print("Invalid input for time-bound. Defaulting to 'no'.")
        time_bound = "no"

    reminder = f"Reminder: '{task}' is a "

    match priority:
        case "high":
            reminder += "high priority task"
        case "medium":
            reminder += "medium priority task"
        case "low":
            reminder += "low priority task"
        case _:
            reminder += "task of unspecified priority"

    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". Consider completing it when you have free time."

    print(reminder)

    another = input("Do you want to input another task? (yes/no): ").lower()
    if another != "yes":
        print("Goodbye!")
        break
