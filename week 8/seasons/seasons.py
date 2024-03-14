from datetime import date
from datetime import datetime
import sys
import inflect
p = inflect.engine()


def main():
    today = date.today()


    # Get user input as a string
    user_input_str = input("Date of Birth: ")

    try:
        # Convert the user input string to a datetime object
        user_input_datetime = datetime.strptime(user_input_str, "%Y-%m-%d")

        # Extract the date part from the datetime object
        user_input_date = user_input_datetime.date()

    except ValueError:
        sys.exit("Invalid date")

    days = today - user_input_date
    minutes = int(days.total_seconds() / 60)

    # Use andword='' to avoid adding "and" between hundreds and tens
    minutes_words = p.number_to_words(minutes, andword='')
    print(f"{minutes_words.capitalize()} minutes")

if __name__ == "__main__":
    main()
