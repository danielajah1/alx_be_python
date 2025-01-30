from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the format 'YYYY-MM-DD HH:MM:SS'.
    """
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format the date and time
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """
    Prompts the user for a number of days and calculates the future date after adding that number of days to the current date.
    """
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()  # Get the current date and time
        future_date = current_date + timedelta(days=days_to_add)  # Add the specified number of days
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Invalid input. Please enter an integer value for the number of days.")

def main():
    """
    Main function to execute the script and demonstrate the use of the datetime module.
    """
    print("Welcome to the DateTime Exploration Script!")
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
