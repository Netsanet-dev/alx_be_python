Python projects

match task:
case if priority == 'high' and time*bound == 'yes':
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
case *:
print('Please enter the correct format')
