import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    regex = r"(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
    if (match := re.search(r"^" + regex + " to " + regex + "$", s)):
        first_hour, first_min, first_meridiem, second_hour, second_min, second_meridiem = match.groups()
        if first_hour == "12":
            if first_meridiem == "AM":
                hour1 = "00"
            else:
                hour1 = "12"
        else:
            if first_meridiem == "AM":
                hour1 = f"{int(first_hour):02}"
            else:
                hour1 = f"{int(first_hour)+12}"
        if first_min == None:
            min1 = "00"
        else:
            min1 = f"{int(first_min):02}"
        time1 = f"{hour1}:{min1}"

        if second_hour == "12":
            if second_meridiem == "AM":
                hour2 = "00"
            else:
                hour2 = "12"
        else:
            if second_meridiem == "AM":
                hour2 = f"{int(second_hour):02}"
            else:
                hour2 = f"{int(second_hour)+12}"
        if second_min == None:
            min2 = "00"
        else:
            min2 = f"{int(second_min):02}"
        time2 = f"{hour2}:{min2}"
        return f"{time1} to {time2}"
    else:
        raise ValueError
if __name__ == "__main__":
    main()


# better answer
# import re
#
#
# def main():
#     print(convert(input("Hours: ")))
#
#
# def convert(s):
#     regex = "(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
#     match = re.search(r"^" + regex + " to " + regex + "$", s)
#     if match:
#         from_time = standardize(match.group(1), match.group(2), match.group(3))
#         time = standardize(match.group(4), match.group(5), match.group(6))
#         return f"{from_time} to {time}"
#     else:
#         raise ValueError
#
#
# def standardize(hr, min, x):
#     if hr == "12":
#         if x == "AM":
#             hour = "00"
#         else:
#             hour = "12"
#     else:
#         if x == "AM":
#             hour = f"{int(hr):02}"
#         else:
#             hour = f"{int(hr)+12}"
#     if min == None:
#         minute = "00"
#     else:
#         minute = f"{int(min):02}"
#     return f"{hour}:{minute}"
#
#
# if __name__ == "__main__":
#     main()