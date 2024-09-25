import datetime
current_date = datetime.datetime.now()
def display_current_datetime():
    print("Current date and time:",datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    x = int(input("Enter the number of days to add to the current date:"))
    future_date = current_date + datetime.timedelta(days = x)
    print("Future date:",future_date)

display_current_datetime()
calculate_future_date()
