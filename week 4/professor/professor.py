import random


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                pass
        except ValueError:
            pass


def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError
    max_value = 10 ** level-1
    return random.randint(0, max_value)


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y

        for _ in range(3):
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")

        else:
            print(f"{x} + {y} = {correct_answer}")

    print(f"Score: {score}")


if __name__ == "__main__":
    main()
# my answer
# import random
#
# def main():
#     while True:
#         try:
#             level = int(input("Level: "))
#         except ValueError:
#             continue  # Ask for input again if it's not an integer
#
#         if get_level(level):
#             correct_answers = 0  # Initialize the counter for correct answers
#             for _ in range(10):
#                 if generate_integer(level):
#                     correct_answers += 1
#             print(f"Score: {correct_answers}")
#             break
#         else:
#             pass
#
# def get_level(level):
#     return isinstance(level, int) and level <= 3
#
# def generate_integer(level):
#     maxnum = 10 ** level
#     x = random.randint(1, maxnum)
#     y = random.randint(1, maxnum)
#     calc = f"{x} + {y} = "
#
#     result = x + y
#     wrong_answers = 0
#
#     while wrong_answers < 3:
#         try:
#             answer = int(input(calc))
#         except ValueError:
#             continue  # Ask for input again if it's not an integer
#
#         if answer == result:
#             return True  # Return True if the answer is correct
#         else:
#             wrong_answers += 1
#     else:
#         print(f"{calc}{result}")
#         return False  # Return False if all attempts are incorrect
#
# if __name__ == "__main__":
#     main()
