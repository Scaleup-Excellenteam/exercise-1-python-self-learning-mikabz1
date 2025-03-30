import random
import datetime

MONDAY = 0
def no_vinnigrete() -> None:
    """generate a random date between to user input date ,
        if the generated date is a monday print proper message ,
        the date format is 'YYYY-MM-DD'"""
    user_date1 = input("enter first date: ")
    user_date2 = input("enter second date: ")

    date_format = '%Y-%m-%d'

    try:
        user_date1 = datetime.datetime.strptime(user_date1, date_format)
        user_date2 = datetime.datetime.strptime(user_date2, date_format)
    except ValueError:
        print("invalid date")
        return None

    # Convert to ordinal numbers
    start = min(user_date1.toordinal(), user_date2.toordinal()) + 1 # Exclude lower bound
    end = max(user_date1.toordinal(), user_date2.toordinal()) - 1 # Exclude upper bound

    random_date = random.randint(start, end)
    random_date = datetime.date.fromordinal(random_date)

    print("the random date is {}".format(random_date))
    if random_date.weekday() == MONDAY:
        print("i don't have vinnigrete")

if __name__ == "__main__":
    no_vinnigrete()