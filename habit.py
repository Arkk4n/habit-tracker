import datetime
import os

if os.path.exists("data.txt"):
    with open("data.txt", "r") as file:
        pass
else:
    with open("data.txt", "w") as file:
        pass

def run_tracker():
    today = datetime.date.today()
    #input - start date
    user_input = input("Enter start date (YYYY-MM-DD): ")
    #validate format
    try:
        year, month, day = user_input.split("-")
        year = int(year)
        month = int(month)
        day = int(day)

    except ValueError:
        print("Invalid date format.")
        return
    start_date = datetime.date(year, month, day)
    delta = today - start_date

    habit = input("What habit are you tracking?: ")
    daily_cost = float(input("How much money do you save per day by not doing this habit?: "))
    days = delta.days
    saved = days * daily_cost

    print("\n========== REPORT ==========")
    print(f"Habit: {habit}")
    print(f"Days clean: {days}")
    print(f"Money saved: {saved:.2f} €")
    print("================================")
run_tracker()