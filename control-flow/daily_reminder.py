c = input("Enter your task:")
pr = input("Priority (high/medium/low):")
t = input("Is it time-bound? (yes/no):")
match pr:
    case "high":
        if t == "yes":
            print(f"Reminder: '{c}' is a high priority task that requires immediate attention today!")
        elif t == "no":
            print(f"Note: '{c}' is a high priority task. Consider completing it when you have free time.")
    case "medium":
        if t == "yes":
            print(f"Reminder: '{c}' is a medium priority task that requires immediate attention today!")
        elif t == "no":
            print(f"Note: '{c}' is a medium priority task. Consider completing it when you have free time.")
    case "low":
        if t == "yes":
            print(f"Reminder: '{c}' is a low priority task that requires immediate attention today!")
        elif t == "no":
            print(f"Note: '{c}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("no result")