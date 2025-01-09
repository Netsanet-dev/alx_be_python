from datetime import datetime, timedelta, date

def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")
    
def calculate_future_date():
    current_date = date.today()
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=number_of_days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")    
    
def main():
    display_current_datetime()
    calculate_future_date()
    
if __name__ == "__main__":
    main()