from datetime import datetime,timedelta
current_date = datetime.now()
def display_current_datetime():
    print("Current date and time:",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    x = int(input("Enter the number of days to add to the current date:"))
    future_date = current_date + timedelta(days = x)
    print("Future date:",future_date.strftime("%Y-%m-%d"))
display_current_datetime()
calculate_future_date()
