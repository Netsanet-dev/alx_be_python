task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        priority = f"'{task}' is a {priority} priority "
    case "medium":
        priority = f"'{task}' is a {priority} priority "
    case "low":
        priority = f"'{task}' is a {priority} priority task. "
    case _:
        print('Please enter the correct format')

if time_bound == "yes":
    print("Reminder: "+priority +" that requires immediate attention today!")
else:
    print(f"Note: {priority} Consider compeleting it when you have free time.")