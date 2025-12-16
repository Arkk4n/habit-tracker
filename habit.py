import datetime
import os


def load_data():
    if not os.path.exists("data.txt"):
        return None

    with open("data.txt", "r") as file:
        line = file.read().strip()
        if not line:
            return None

        habit, start_date, daily_cost = line.split(",")
        return habit, start_date, float(daily_cost)


def save_data(habit, start_date_str, daily_cost):
    with open("data.txt", "w") as file:
        file.write(f"{habit},{start_date_str},{daily_cost}")


def get_start_date():
    user_input = input("Enter start date (YYYY-MM-DD): ")

    try:
        year, month, day = user_input.split("-")
        start_date = datetime.date(int(year), int(month), int(day))
        return start_date
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return None


def get_habit_info():
    habit = input("What habit are you tracking?: ")

    try:
        daily_cost = float(input("How much money do you save per day by not doing this habit?: "))
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
    print("============================")


def main():
    stored = load_data()
    if stored:
        habit, start_date_str, daily_cost = stored
        print(f"Last tracked habit: {habit} (since {start_date_str}), daily save: {daily_cost} €")

    start_date = get_start_date()
    if start_date is None:
        return

    habit, daily_cost = get_habit_info()
    if habit is None or daily_cost is None:
        return

    days, saved = calculate_report(start_date, daily_cost)
    print_report(habit, days, saved)

    save_data(habit, start_date.isoformat(), daily_cost)


main()