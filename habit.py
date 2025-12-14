import datetime


def get_start_date():
    today = datetime.date.today()
    # input - start date
    user_input = input("Enter start date (YYYY-MM-DD): ")
    # validate format
    try:
        year, month, day = user_input.split("-")
        year = int(year)
        month = int(month)
        day = int(day)
    except ValueError:
        print("Invalid date format.")
        return None


def get_habit_info():
    habit = input("What habit are you tracking?: ")
    try:
        daily_cost = float(input("How many days would you like to track?: "))
        return habit, daily_cost
    except ValueError:
        print("Daily cost must be a number.")
        return None, None


def calculate_report(start_date, daily_cost):
    today = datetime.date.today()
    delta = today - start_date
    days = delta.days
    saved = days * daily_cost
    return days, saved

def print_report(habit, days, saved):
    print("\n========== REPORT ==========")
    print(f"Habit: {habit}")
    print(f"Days clean: {days}")
    print(f"Money saved: {saved:.2f} €")
    print("================================")

def main():
    start_date = get_start_date()
    if start_date is None:
        return
        habit, daily_cost = get_habit_info()
    if habit is None or daily_cost is None:
        return
    days, saved = calculate_report(start_date, daily_cost)
    print_report(habit, days, saved)

    main()





