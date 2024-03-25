import re
import validators

def main():
    print(email_validator(input("What's your email address? ")))


def email_validator(email):

    if validators.email(email):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
