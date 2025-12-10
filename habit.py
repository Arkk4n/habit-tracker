import datetime

today = datetime.date.today()


user_input = input("Enter start date (YYYY-MM-DD): ")
year, month, day = user_input.split("-")
year = int(year)
month = int(month)
day = int(day)
start_date = datetime.date(year, month, day)
delta = today - start_date



habit = input("What habit are you tracking?: ")
daily_cost = float(input("How much money do you save per day by not doing this habit?: "))
days = delta.days
saved = days * daily_cost

print(f"You have been free from {habit} for {days} days.\nYou have saved {saved:.2f} euros.")