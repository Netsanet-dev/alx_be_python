task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time = input("Is it time-bound? (yes/no): ")

match (priority, time):
    case ('high', 'yes'):
        print(f"'{task}' is a {priority} priority task that requires immediate attention today!")
    case ('medium', 'yes'):
        print(f"'{task}' is a {priority} priority task that requires medium attention today!")
    case ('low', 'yes'):
        print(f"'{task}' is a {priority} priority task that requires low attention today!")
    case ('high', 'no'):
        print(f"'{task}' is a {priority} priority task that requires attention but complete when you have free time.")
    case ('medium', 'no'):
        print(f"'{task}' is a {priority} priority task that requiers medium attention, complete when you have free time.")
    case ('low', 'no'):
        print(f"'{task}' is a {priority} priority task. Consider completing it when you have free time.")
    case _:
        print('Please enter the correct format')
